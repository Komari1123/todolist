from django.db import models
import datetime

# Create your models here.

PRIORITY=(('danger','high'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    titile = models.CharField(max_length = 100)
    author = models.CharField(max_length=100)
    author_pk = models.IntegerField()
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY,
        )
    duedate = models.DateField()
    start_time = models.TimeField(default=datetime.time(0, 0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0, 0))
    def __str__(self):
        return self.titile