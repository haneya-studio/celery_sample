import os
import datetime
import django
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # プロジェクト名を適宜変更
app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

django.setup()

@app.task
def sample_task():
  from weather.models import Log
  print(f"タスク実行: {datetime.datetime.now()}")
  Log.objects.create(target="sample_task")
  return "Task Completed"

@app.task
def fetch_weather():
  from weather.models import Log
  print(f"天気取得: {datetime.datetime.now()}")
  Log.objects.create(target="天気")
  return "天気取得完了"

