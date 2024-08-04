import os

os.system("python3 manage.py collectstatic")
os.system("python3 manage.py runserver")