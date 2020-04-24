from django.db import models

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
    def __str__(self):
        return self.titile