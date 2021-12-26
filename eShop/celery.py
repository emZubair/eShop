import os
from celery import Celery

# set the Default setting module for the 'Celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eShop.settings')

app = Celery('eShop')

app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()
