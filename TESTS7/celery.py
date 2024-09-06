import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TESTS7.settings')
app = Celery('TESTS7')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()