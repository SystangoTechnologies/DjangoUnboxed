from celery import shared_task


@shared_task
def add(a, b):
    return a + b
