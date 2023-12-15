# Django Web Face
## By Chau The Khanh 


## Feature

<h4>Part 1:</h4>
<ol>
    <li>Create a web-app where a user can login.</li>
    <li>User can upload files.</li>
    <li>User can view his/her uploaded files.</li>
</ol>

<h4>Part 2:</h4>
<ol>
     <li>User can search and view profile of other users.</li>
     <li>They can share their uploaded files with any of those users.</li>
     <li>Users can see the shared files by other users also in uploaded files.</li>
</ol>

<h4>Additional Features:</h4>
<ol>
    <li>In users profile user can set his/her profile picture.</li>
    <li>Users can download other users uploaded files.</li>
    <li>The user can upload any type of files such as images, videos, text files and also different types of programs like python code, java code, etc.</li>
</ol>
    
<h2>Technologies Used:</h2>
<ul>
    <li>Python 3.8</li>
    <li>Django 4.2</li>
    <li>Bootstrap</li>
    <li>JavaScript</li>
</ul>
    
<h2>Additional Python Modules Required:</h2>
<ul>
    <li>django-crispy-forms 2.1</li>
    <li>crispy-bootstrap4 2023.1</li>
    <li>Pillow 10.1.0</li>
</ul>
  
<h2>Note :</h2>

<b>The Secret_Key required for the execution and debugging of project is not removed from the project code. So you can use the project as your college mini-project or by using the project code you can build your own project.</b>

<h2>Usage :</h2>

    python django_web_app/manage.py makemigrations

    python django_web_app/manage.py migrate

    python django_web_app/manage.py runserver
    
   In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/

## I. Install basic things
### 1. Setup new Django project
- Let’s create a new Django project with command:
```bash
django-admin startproject DjangoWebFace
```

### 2. Setup new Django app for blog
- Run following commands to create new Django app tutorials:
```bash
cd DjangoWebFace
python manage.py startapp blog
```

### 3. Migrate Data Model to the database
- Run the Python script:
```bash
cd DjangoWebFace
python manage.py makemigrations blog
```
- To apply the generated migration above, run the following Python script:
```bash
python manage.py migrate blog
```

### 4. Run

```bash
python manage.py runserver 8080
```
It starts development server at `http://127.0.0.1:8080/` or `http://localhost:8080/`.

