# Hospital 

This is small Django project written in python3. The goal of this is to emulate hospital databse. User can edit each table from web page. 
## Getting Started

### Prerequisites

Needed libraries. Instalation steps was tested on Ubuntu 18.04.
postgres database.
```
sudo apt-get update
sudo apt-get install python-pip3 python-dev libpq-dev postgresql postgresql-contrib 
```
Django
```
pip3 install django psycopg2 django-widget-tweaks django-filter django-crispy-forms factory_boy
```

### Create a Database and Database User

```
sudo su - postgres
psql
```
Next create database.
```
CREATE DATABASE hospital;
```
Create user. If you want to change user name and password you schould also change values inside mysite/settings DATABASE configuration.
```
CREATE USER my_user WITH PASSWORD '123456789';
```
Setup user.
```
ALTER ROLE my_user SET client_encoding TO 'utf8';
ALTER ROLE my_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE my_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE hospital TO my_user;
```
Finally exit.
```
\q
exit
```
### Setup django migrations
Go to mysie directory. Execute:
```
python3 manage.py makemigrations
```
This schould print something simillar to:
```
Migrations for 'hospital':
  hospital/migrations/0001_initial.py
    - Create model Appointment
    - Create model BankAccount
    ...
```
Next type and hit enter:
```
python3 manage.py migrate
```
Optionaly if you want populate database with some random data you can execute:
```
python3 manage.py populate_db 10
```
This will create at leat 10 rows for each table in database.



## Runnig server
In order to start server execute:
```
python3 manage.py runserver
```
After this go to http://127.0.0.1:8000/hospital/
## Authors

* **Lukasz Eckert** - *Initial work* 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

