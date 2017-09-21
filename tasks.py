from celery import Celery

app = Celery('tasks', broker='amqp://')

@app.task
def add(x, y):
    return x + y