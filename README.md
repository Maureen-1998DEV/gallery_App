# Projects Name:
##  MyGallery_App

## Contributors
    - Maureen Ougo

### Contact Information
ougomaureen051@gmail.com
## Description

MyGallery is my first project of django it showcases pictures in category ,location.

## Features
- The home page allows users to see various images:
- User can see all images per location they were taken
- Users can also search for images in categories
- Admin can upload images from a django dashboard

## View Live Site here
View the complete site [here](https://ougo-gallery.herokuapp.com/)

## Technologies Used
    - Python 3.8
    - Django MVC framework
    - HTML, CSS and Bootstrap
    - JavaScript
    - Postgressql
    - Heroku

## Specifications
To view the user dtories or BDD check the [specs file](specs.md).

### Prerequisite
MyGallery requires a prerequisite understanding of the following:

- Python3.8
- Postgres
- Python virtualenv
- Django Framework
## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE mygallery;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'mygallery'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.8 manage.py makemigrations gallery
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000

## Known bugs
No known bugs so far.



