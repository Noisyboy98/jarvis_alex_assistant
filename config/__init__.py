import json
import os
import platform

fo = open("assistant_config.json", "r+", encoding="utf8")
data = json.load(fo)
assistant_config = []
for assistant in data['assistant']:
    if assistant['active'] == 1:
        assistant_config = assistant
        break 
fo.close()
APP_DETAILS_FILE = 'config/applications.json'

with open('config/config'+assistant_config['name']+'.json', encoding="utf8") as file:
    DATA = json.load(file)

if os.path.exists(APP_DETAILS_FILE) is False:
    with open(APP_DETAILS_FILE, 'w') as file:
        file.write('{}')