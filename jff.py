import utils
import config
import json
import threading


f = open('datachatAlex.json', encoding='utf-8')

data = json.load(f)
storequestions = []
storeAnswers = []
break_word = ' ủa'
for each in data:
    if break_word in each['questions']:
        storequestions.append(each['questions'])
        storeAnswers.append(each['answers'])

with open("test1.json","w", encoding='utf-8') as jsonfile:
        json.dump(storequestions,jsonfile,ensure_ascii=False)
with open("test2.json","w", encoding='utf-8') as jsonfile:
        json.dump(storeAnswers,jsonfile,ensure_ascii=False)