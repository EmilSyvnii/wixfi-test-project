from celery import shared_task
import time


@shared_task
def run_simple_task():
    print('Start task')
    time.sleep(5)
    print('Finish task')
