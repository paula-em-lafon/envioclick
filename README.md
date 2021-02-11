# Envio Click test #

# Part One #

There is two files: `prueba1.py` and `prueba2.py` these have been set up to run
the test cases in the document. You can open them to check them

# Part Two #

The diagram for the database is called `waiters.png`, it's on the home folder.

The database migrations and methods have been done according to instructions. 
To run you must initialize a virtual env and do: `pip install -r requirements.txt`.

run the server by doing:

`cd restaurant`

`python manage.py runserver`

The server will run on 127.0.0.1:8000

You can add services to the available tables (already populated in sqlite database)
by going to 127.0.0.1:8000/admin.

if there is a super user created the username is `admin` and the password is `admin`

else, create a superuser by running:

`python manage.py createsuperuser`

In the admin there's already a number of tables (4) and a number of waiters (1).
you can create services by going to the add service section in the admin.

You only need to fill out the tip, the rest is done automatically.

If it's between 9:00 and 11:30 pm the service will be created if there's waiters and tables available. There is no need to fill the fields, the create function does it automatically and
randomly.

if There's not enough tables, waiters or the restaurant is closed a ValidationError will be returned and the database entry will not be created

### testing ###
From the restaurant root folder run

`python manage.py test`

## Part Three ##

The tests for the problem are defined in the file `pdftesting`


## Thank you very much :) ##