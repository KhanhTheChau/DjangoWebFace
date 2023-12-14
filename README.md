# DjangoWebFace
## By Chau The Khanh 


### Technology
- Python 3.8
- Django 4.2


### 1. Setup new Django project
- Let’s create a new Django project with command:
```bash
django-admin startproject DjangoWebAPI
```

### 2. Setup new Django app for blog
- Run following commands to create new Django app tutorials:
```bash
cd DjangoWebAPI
python manage.py startapp blog
```

### 3. Migrate Data Model to the database
- Run the Python script:
```bash
cd DjangoWebAPI
python manage.py makemigrations blog
```
- To apply the generated migration above, run the following Python script:
```bash
python manage.py migrate blog
```
