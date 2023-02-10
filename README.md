# Bulk-Mailer-Backend

A Django based backend system for bulk mailing using PostgreSQL, Celery, Nginx, Gunicorn, and deployed on a virtual machine.

## FEATURES

- Django as a web framework for the backend
- PostgreSQL as the database
- Celery for task management and scheduling of bulk mailing
- Nginx as a reverse proxy server
- Gunicorn as a Python WSGI HTTP Server
- Deployed on Azure virtual machine
- Template based emails
- Ability to bulk upload data from CSV, Excel
- Celery beat for updating the status of the emails
- JWT Authentication for secure API access

## RUNNING THE SERVER


1. Clone the repository:

```CMD
git clone https://github.com/suhaillahmad/Bulk-Mailer-Backend.git
```
To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.


2. Install, Create and activate a virtual environment:

```CMD
pip install virtualenv
virtualenv venv
```
Activate the virtual environment
```CMD
source venv/bin/activate
```


3. Install the dependencies: 

```CMD
pip install -r requirements.txt
```


4. Setup .env file in cryptBEE/cryptBEE and navigate back to base directory cryptBEE/

```
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

DBPASSL = ''
DBHOSTL = ''
DBNAMEL = ''
DBUSERL = ''
```


5. Create a PostgreSQL database and connect it by entering credentials in .env file, once connected run the migrate command
```CMD
python manage.py migrate
```


6. Run the backend server on localhost:

```CMD
python manage.py runserver
```


You can access the endpoints from your web browser following this url
```url
http://127.0.0.1:8000
```


7. You can create a superuser executing the following commands
```CMD
python manage.py createsuperuer
```
A prompt will appear asking for email followed by password. 
To access the django admin panel follow this link and login through superuser credentials
```url
http://127.0.0.1:8000/admin/
```


8. Start the Celery worker (On a separate terminal with activated virtual environment):
```CMD 
celery -A bulkmailer.celery worker --pool=solo -l info
```


9. Run celerybeat (On a separate terminal with activated virtual environment):

```CMD
celery -A bulkmailer beat -l info
```





