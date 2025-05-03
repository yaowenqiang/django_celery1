from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='rpc://',)
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y
