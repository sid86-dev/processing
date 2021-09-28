from flask import Flask
from flask_celery import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://:J9BmwAzuZuFNHY6Xg6u2pXRci0dJRnkH@redis-12393.c10.us-east-1-4.ec2.cloud.redislabs.com:12393/10628127'

app.config['CELERY_RESULT_BACKEND'] = 'redis://:J9BmwAzuZuFNHY6Xg6u2pXRci0dJRnkH@redis-12393.c10.us-east-1-4.ec2.cloud.redislabs.com:12393/10628127'

celery = make_celery(app)

@app.route('/')
def home():
    return 'This is celery flask'

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return f"Request sent"

@celery.task(name='celery_example.reverse')
def reverse(string):
    s = string[::-1]
    return s

if __name__=='__main__':
    app.run()