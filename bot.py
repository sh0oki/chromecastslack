from slackclient import SlackClient
import json
import os

ICON = ":guitar:"

class Bot(object):
    def __init__(self):
        self._client = SlackClient(self._token())
        self._icon = ICON
        self._client.rtm_connect()

    def _token(self):
        return os.environ['SLACKBOT_TOKEN']
    
    def _channel(self):
        return os.environ['CHANNEL']

    def _username(self):
        return os.environ['USERNAME']

    def say(self, message):
        self._client.rtm_send_message(self._channel, message)

    def sayEx(self, text, image, footer):
        d = {'thumb_url': image, 'text': text, "footer": footer, "fallback": text}
        self._client.api_call("chat.postMessage", channel=self._channel(), username=self._username(), as_user="false", icon_emoji=self._icon, attachments=json.dumps([d]))

