# Generated by Django 3.2.3 on 2021-06-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0004_task_bucket'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completedItems',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='totalItems',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
