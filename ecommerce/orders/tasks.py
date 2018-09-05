# from celery import Celery

# app = Celery('tasks', broker='pyamqp://guest@localhost//')

# @app.task
# def add(x, y):
#     return x + y

from __future__ import absolute_import, unicode_literals
from celery import task
from django.core.mail import send_mail


@task()
def task_number_one():
    send_mail(
    'Ordered',
    'ordered.',
    'alexsam374@gmail.com',
    ['falgunbalachandran@gmail.com'],
    fail_silently=False
    )