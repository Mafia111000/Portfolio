# Django
django-admin startproject MAFIA
python manage.py startapp home
python manage.py runserver



python manage.py makemigrations
python manage.py migrate
#make super user
python manage.py createsuperuser

REGISTER MODEL
if making models change after working in Models
add that to admin.py 

from home.models import contacts
admin.site.register(contacts)

REGISTER APP
also. take class name from apps.py to settings.py
enter an entry 
home.apps.{copied name} in INSTALLED_APPS

getting data from database

from home.models import ____

contact.objects.all()  # lsit dega ye objects ka, so can be used as..
contact.objects.all()[0].name
contact.objects.filter(name='mafia') # ye bhi list dega
