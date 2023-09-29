import utils
import config
import wikipedia
from translate import Translator

class Definition:

    def __init__(self, command, response):
        self.os = config.assistant_config['name']
        self.language = config.assistant_config['language']
        self.command = command
        self.response = response

    def launch(self):
        things = utils.get_search_value(self.command,'Definition')
        translator_things = Translator(from_lang= self.language, to_lang='en-EN')
        things = translator_things.translate(things)
        print(things)
        info = wikipedia.summary(things,1)
        translator = Translator(to_lang=self.language)
        tran_info = translator.translate(info)
        print(tran_info)
        utils.speak(tran_info .format(things = tran_info))