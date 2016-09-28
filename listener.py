#!/usr/local/bin/python3.5

from time import sleep
import logging
import schedule

import pychromecast
import bot

POLL_INTERVAL = 1800

class ChromecastListener(object):
    def __init__(self, player, bot):
        self._song = None
        self._player = player
        self._bot = bot

    def new_media_status(self, status):
        logging.debug("[%s] Got new_media_status %s" % (self._player, status.player_state))
        if status.player_state != 'PLAYING':
            logging.debug("[%s] Skipping due to status" % (self._player,))
            return

        if status.media_metadata['songName'] == self._song:
            logging.debug("[%s] Skipping due to same song again (%s)" % (self._player, self._song))
            return

        self._song = status.media_metadata['songName']
        logging.info("Posting song %s" % (self._song, ))
        try:
                self.postSong(status.media_metadata['artist'], status.media_metadata['songName'], status.media_metadata['images'][0]['url'])
        except Exception as e:
                logging.exception("Failed to post song")

    def postSong(self, artist, song_name, image=None):
        logging.info("[%s]\t%s - %s (%s)" % (self._player, artist, song_name, image))
        self._bot.sayEx("%s - %s" % (song_name, artist), image, self._player)

def active_devices():
    return pychromecast.get_chromecasts_as_dict().keys()

class ChromecastManager(object):
    def __init__(self, bot):
        self.active_list = {}
        self.bot = bot

    def poll(self):
        for chromecast in active_devices():
            if chromecast in self.active_list:
                continue
            self.register(chromecast)

    def register(self, chromecast):
        l = ChromecastListener(chromecast, self.bot)
        cs = pychromecast.get_chromecast(friendly_name=chromecast)
        cs.wait()
        mc = cs.media_controller
        mc.register_status_listener(l)
        logging.info("[%s] Registered" % (chromecast, ))
        self.active_list[chromecast] = [l, mc]

def main():
    m = ChromecastManager(bot.Bot())
    while True:
        m.poll()
        sleep(POLL_INTERVAL)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

