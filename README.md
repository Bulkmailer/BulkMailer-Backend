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

<img width="1440" alt="Screenshot 2023-03-20 at 2 34 32 AM" src="https://user-images.githubusercontent.com/97229491/226208926-b92682b8-03ab-4d3e-8775-79cb54d53531.png">

![2B28863B-D505-41F8-A10A-C7722D0BA664_1_201_a](https://user-images.githubusercontent.com/97229491/226208578-7db4c108-0c8c-44cc-bfa7-0a35785a35aa.jpeg)
![BB49E170-CCA7-4294-B6A9-B1BA5121E07E_1_201_a](https://user-images.githubusercontent.com/97229491/226208619-181556e5-1a0f-45b3-a26e-72980db6da90.jpeg)
![607025F3-6FF6-4104-ADA7-8360288689A6_1_201_a](https://user-images.githubusercontent.com/97229491/226208654-70d9dbd4-1e3a-4d40-ba52-c12d494df322.jpeg)
![A04885EC-14CA-4B66-8095-235B39429D13_1_201_a](https://user-images.githubusercontent.com/97229491/226208678-13847966-e0ac-44ba-9aa7-931d62570a52.jpeg)
![59B79916-9771-4B25-A5CE-851CB7EFF57B_1_201_a](https://user-images.githubusercontent.com/97229491/226208718-b1319321-0d23-4853-b37b-316c6f1b3e63.jpeg)
![43FCD5C3-7876-4E7A-BD83-C5F693FCA609_1_201_a](https://user-images.githubusercontent.com/97229491/226208846-adc0ffe5-4f6c-4096-89b3-a1ade165adb9.jpeg)

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

4. Setup .env file in Bulk-Mailer-Backend/bulkmailer

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
