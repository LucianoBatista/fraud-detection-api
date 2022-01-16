import time

from src import celery
from celery import shared_task


@shared_task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    print("Done")
    return True
