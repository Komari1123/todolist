from django.db import models
import datetime

# Create your models here.

PRIORITY=(('danger','high'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    titile = models.CharField(max_length = 100)
    author_pk = models.IntegerField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY,
        )
    start_time = models.TimeField(default=datetime.time(0, 0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0, 0))
    predict_pomodoro = models.IntegerField(default=0)
    true_pomodoro = models.IntegerField(default=0)
    def __str__(self):
        return self.titile