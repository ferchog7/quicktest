# TEST QUICK #

### Requirements

- pip install Django
- pip install djangorestframework

## Running

With requirements installed run, port(8080) is optional:

    $ python manage.py runserver 8080

## Database

Run the migrations to implement the database model and generate a superuser:

    $ python manage.py migrate
    $ python manage.py createsuperuser

## API TEST

You can use the following Postman collection:

    https://www.getpostman.com/collections/c4ef915ff4934f22ba44

## Login

Use the url 'http://localhost:8080/login' to generate your token with the access data given to the generated superuser.

## Endpoints

- clients/
- products/
- bills/
- report/
