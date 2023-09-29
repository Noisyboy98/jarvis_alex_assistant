import utils
import config
import os
import json

class Changeos:

    def __init__(self, command, response):
        self.os = config.assistant_config['name']
        self.command = command
        self.response = response

    def launch(self):
        fo = open("assistant_config.json", "r+", encoding="utf8")
        data = json.load(fo)
        for assistant in data['assistant']:
            if assistant['active'] == 1:
                assistant['active'] = 0
            elif assistant['active'] == 0:
                assistant['active'] = 1
        with open("assistant_config.json","w", encoding='utf-8') as jsonfile:
            json.dump(data,jsonfile,ensure_ascii=False)
        fo.close()
        utils.speak(self.response)
        os.system("python main.py")
        exit()