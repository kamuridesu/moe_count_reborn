import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moe_count.settings")
app = Celery("moe_count")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()