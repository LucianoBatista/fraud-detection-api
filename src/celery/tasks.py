import time

from src import celery
from celery import shared_task


@shared_task(name="async_workflow")
def async_workflow(download_link: str, training_queue_id: int):
    from src.pipelines.main import run_pipeline

    run_pipeline(download_link=download_link, training_queue_id=training_queue_id)
