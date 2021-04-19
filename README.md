# library-api

## Description

This is a django application for used for managing a catalogue of books. Books:
* Can be created 
* Edited (title, description,author,etc)
* Loaned

In addition to managing books this application can also help manage/maintain author details,genres and book titles in different languages

## Quick start
The application can be accesed at https://limitless-spire-67788.herokuapp.com/ . For the purposes of testing the following credentials can be used to login and play around with the application

### Normal user credentials
* username: tester
* password: testerpassword

### Staff credentials (Admin)
* username: admin
* password: admin19940 

## Project models
![UML](https://raw.githubusercontent.com/Burugux/library-api/main/library_model_uml.png)

## Requirements
* Python 3.6
* pip
* virtualenv
* Postgres

# Installation
### 1)Clone the repo from GitHub:
```console
$ git clone https://github.com/Burugux/library-api.git
```

### 2) Create a virtual environment and install the necessary packages with:
```console
$ virtualenv -p python3 env
```

or
```console
$ python3 -m venv env
```

### 3) Activate virtual environment:
```console
$ source env/bin/activate
```

### 4) cd to the root of the api:
```console
$ cd rental_api
```

### 5) Install requirements:
```console
$ pip install -r requirements.txt
```

### 6) Make migrations:
```console
$ python manage.py makemigration
$ python manage.py migrate
```

# Users
#### Create a superuser who can access the dashboard
```console
$ python manage.py createsuperuser
```

# Admin dashboard
Normal Users,books,authors,genres,languages and book instances can be added via the admin dashboard

# start the development server
Create a superuser who can access the admin dashboard https://limitless-spire-67788.herokuapp.com/admin/
```console
$ python manage.py runserver
```

# Running the tests
```console
$ coverage run --source='.' manage.py test books
```
