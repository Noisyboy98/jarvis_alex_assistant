import utils
import config
import json
import nltk
from model.model_training import TrainingModel

class Chat:
    def __init__(self, command, response):
        self.os = config.assistant_config['name']
        self.error = config.assistant_config['error']
        self.language = config.assistant_config['language']
        self.command = command
        self.response = response
        self.words = []
        self.classes = []
        self.data_x = []
        self.data_y = []

    def launch(self):
        f = open('testAlex.json', encoding="utf8")
        self.DATA = json.load(f)
        for intent in self.DATA['intents']:
            for utterance in intent['utterances']:
                tokens = nltk.word_tokenize(utterance)
                self.words.extend(tokens)
                self.data_x.append(utterance) 
                self.data_y.append(intent['tag'])
            if intent['tag'] not in self.classes:
                self.classes.append(intent['tag'])
        self.words = sorted(set(self.words))
        self.classes = sorted(set(self.classes))
        training_model = TrainingModel(self.words, self.classes, self.data_x, self.data_y)
        trained_model = training_model.train()
        pre_intent = ''
        while True: 
            questions = input('user : ')
            break_word = ['break','dừng','stop','ngưng']
            intent = training_model.get_intent(trained_model, questions)
            response = TrainingModel.get_data_type(intent , self.DATA, 'response')
            if any(key in questions for key in break_word) or questions == '':
                utils.speak(response .format(assistant_name = self.os))
                break
            else :
                if intent :
                    if pre_intent != intent or pre_intent == '':
                        # NormalTag, return normal responses
                        pre_intent = intent
                    #elif  pre_intent != '' and intent == 'QuestionBack' :
                        #   print('elif')
                        #  response = TrainingModel.get_data_type(intent, self.DATA, 'response')
                    else :
                        # DoubleTag, return question that ask back user
                        response = TrainingModel.get_data_type('DoubleTag', self.DATA, 'response')
                else :
                    # Return not underst and when not have intent (mostly impossible)
                    response = TrainingModel.get_data_type('NotUnderstand', self.DATA, 'response')
                print(self.os+' :intent = '+intent+ '\n response = ' +response)
                utils.speak(response .format(assistant_name = self.os))