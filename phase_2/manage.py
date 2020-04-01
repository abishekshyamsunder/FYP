#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

def main():
    count = 0
    if count==0:
        os.system('lsof -nti:5055 | xargs kill -9')
        os.system('lsof -nti:5002 | xargs kill -9')
        print('Finished killing all processes, clean start now')
        #subprocess.Popen('cd /Users/abishek/Desktop/final-year-project/TS\ Work/phase_2/rasa && rasa run actions',shell=True)
        #subprocess.Popen('cd /Users/abishek/Desktop/final-year-project/TS\ Work/phase_2/rasa && rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml',shell=True)
        subprocess.Popen('python3 startallservers.py',shell=True)
        #subprocess.Popen('cd /Users/abishek/Desktop/final-year-project/TS\ Work/phase_2/rasa && rasa shell',shell=True)
        count = count + 1
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FYP.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
