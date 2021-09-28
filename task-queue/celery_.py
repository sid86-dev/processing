from celery import Celery
from flask_celery import make_celery
import time

app = Celery('task',
backend='redis://:J9BmwAzuZuFNHY6Xg6u2pXRci0dJRnkH@redis-12393.c10.us-east-1-4.ec2.cloud.redislabs.com:12393/10628127',
broker='redis://:J9BmwAzuZuFNHY6Xg6u2pXRci0dJRnkH@redis-12393.c10.us-east-1-4.ec2.cloud.redislabs.com:12393/10628127')


@app.task()
def task():
    print('starting job .... ')
    time.sleep(4)
    print('task completed')
