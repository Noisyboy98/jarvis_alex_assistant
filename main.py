import speech_recognition as sr
import config
import intents
import model
import utils
import sys

from intents.alarm import Alarm
from intents.translation import Translation
from intents.playsong import Playsong
from intents.chat import Chat
from intents.changeos import Changeos
from intents.time import Time
from intents.definition import Definition
from intents.readnews import Readnews
from intents.weather import Weather
from model.model_training import TrainingModel


def read_voice_cmd(recognizer):
    voice_input = ''
    language = config.assistant_config['language']
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source=source, timeout=5, phrase_time_limit=5)
        voice_input = recognizer.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY",language = language)
        print('Input : {}'.format(voice_input))
    except sr.UnknownValueError: pass
    except sr.RequestError: print('Network error.')
    except sr.WaitTimeoutError: pass
    except TimeoutError: pass
    return voice_input.lower()


def runMain(command, response):
    makeClass = getattr(sys.modules[__name__], 'intent' +intent)(command, response)
    launch = getattr(makeClass, 'launch')
    launch()

if __name__ == '__main__':
    training_model = TrainingModel(model.words, model.classes, model.data_x, model.data_y)
    #print('model.words')
    #print(model.words)
    trained_model = training_model.train()
    recognizer = sr.Recognizer()
    #bootup = TrainingModel.get_data_type('Bootup', config.DATA, 'response')
    #utils.speak(bootup .format(username = config.assistant_config['call']))
    while True:
        #command = read_voice_cmd(recognizer)
        command = input('cmd : ')
        #command = 'chat'
        if command:
            intent = training_model.get_intent(trained_model, command)
            response = TrainingModel.get_data_type(intent, config.DATA, 'response')
            if intent == 'Greeting' or intent == 'Introduce' or intent == 'Capacities':
                utils.speak(response .format(name = config.assistant_config['name']))
            elif intent:
                try:
                    print('intent' +intent)
                    runMain(command, response)
                except Exception as exception:
                   utils.speak(TrainingModel.get_data_type('Error', config.DATA, 'response'))
                    
