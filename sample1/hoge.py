from celery import Celery
from celery import shared_task

app = Celery('tasks', broker='redis://localhost:6379/0', broker_connection_retry=True)
app.conf.result_backend = 'redis://localhost:6379/0'

app.conf.broker_connection_retry_on_startup = True
app.conf.broker_connection_retry = True  # 再試行を有効化
app.conf.broker_connection_max_retries = 5  # 最大5回まで再試行（必要に応じて変更）
app.conf.broker_connection_retry_delay = 5.0  # 再試行の間隔を5秒に設定（必要に応じて変更）

@shared_task
def sub(x, y):
    from time import sleep
    sleep(10)
    return x - y
