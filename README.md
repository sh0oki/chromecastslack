# chromecastslack
Report your playing songs to slack!

This script will look for active Chromecasts in your LAN, then report the currently played song to a slack channel of your choosing.

I tested this script with Python 3.5. Other versions (3.0 and up) should work, but haven't been tested.

## Setup
1. Have a working Chromecast in your LAN, playing music from your favorite source (Spotify, Soundcloud, ...).
1. [Create a bot user](https://my.slack.com/services/new/bot) in your Slack account.
1. Install *chromecastslack* on any computer in your LAN. 
1. Use the API token (*xoxb-a-b*) to execute the bot.

## Installing
```
git clone git@github.com:sh0oki/chromecastslack.git
cd chromecastslack
pip3.5 install -r ./requirements.txt
```

## Usage
```
SLACKBOT_TOKEN=xoxb-my-token CHANNEL=musicreactions USERNAME=Discobear python3.5 listener.py
```
Use your favorite init script to execute the script after restart.
*CHANNEL* and *USERNAME* variables are optional, their default values are shown above.

## Example

<img src="https://github.com/sh0oki/chromecastslack/raw/master/examples/screenshot.png" alt="Screenshot" title="One Look is Worth A Thousand Words" width="657" height="98" />
