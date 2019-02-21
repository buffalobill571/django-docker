from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone



@shared_task
def hello(name):
    # TODO remove me
    print(f'Hello {name}')
    return name

@periodic_task(run_every=crontab(minute='*'))
def hello_world():
    # TODO remove me
    print('hello world')
    return 'hello world'
