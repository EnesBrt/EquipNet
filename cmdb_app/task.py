# In your_app/tasks.py
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.core.management import call_command


@periodic_task(run_every=(crontab(minute="*/5")))
def check_equipment_status():
    from django.core.management import call_command

    call_command("network")
