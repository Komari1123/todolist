# Generated by Django 3.0.3 on 2020-04-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20200425_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='predict_pomodoro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='true_pomodoro',
            field=models.IntegerField(default=0),
        ),
    ]
