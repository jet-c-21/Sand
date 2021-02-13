# Sand
scrape and display the data with Django
------
<br>

## Development Recording
##### 1. create django project
```shell script
// beware you are in the project root dir
django-admin startproject sand .
```
##### 2. create the first app
```shell script
django-admin startapp my_app
```

##### 3. register the app in ```sand/settings.py```
```python
INSTALLED_APPS = [
    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom
    'my_app'
]
```

##### 4. building admin page
```shell script
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```