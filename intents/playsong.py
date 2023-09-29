import pywhatkit
import feedparser
import config
import utils
import keyboard
import time
from random import choice

class Playsong:

    def __init__(self, command, response):
        self.os = config.assistant_config['name']
        self.qs_back = config.assistant_config['qs_back']
        self.command = command
        self.response = response
        
    def launch(self):
        utils.speak(self.qs_back)
        song = input('song = ')
        song = utils.get_search_value(song,'Playsong')
        print(song)
        key_song = ['random','choose','bừa','tùy','chọn']
        if any(key in song for key in key_song):
            song = ''
            while song == '' :
                channel_url = feedparser.parse("https://www.youtube.com/feeds/videos.xml?playlist_id=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj")
                song = choice(channel_url.entries).title
                print(song)
        utils.speak(self.response .format(song = song))
        pywhatkit.playonyt(song)
        # close tab when play 240sec
        #time.sleep(240)
        #keyboard.press_and_release('ctrl+w')
