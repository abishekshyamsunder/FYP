import os
import sys
import subprocess
os.system('lsof -nti:5055 | xargs kill -9')
os.system('lsof -nti:5002 | xargs kill -9')
print('Finished killing all processes, clean start now')
subprocess.Popen('cd rasa && rasa run actions',shell=True)
subprocess.Popen('cd rasa && rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml',shell=True)