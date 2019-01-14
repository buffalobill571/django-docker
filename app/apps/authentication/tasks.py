from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task


@shared_task
def hello(name):
    print(f'Hello {name}')
    return name

@periodic_task(run_every=crontab(minute='*'))
def hello_world():
    print('hello world')
    return 'hello world'
