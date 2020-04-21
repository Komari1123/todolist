from django.db import models

# Create your models here.
class TodoModel(models.Model):
    titile = models.CharField(max_length = 100)
    memo = models.TextField()