import os
os.system("pip install django")
os.system("python manage.py collectstatic")
os.system("python manage.py runserver")
