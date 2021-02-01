import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wixfi_test_api.settings')

# app = Celery('app')
app = Celery('wixfi_test_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
