from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from bulkmailer import settings
from datetime import datetime
from pytz import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bulkmailer.settings')

app = Celery('bulkmailer')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

#CELERY BEAT SETTINGS

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')