# Generated by Django 3.2.3 on 2021-06-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0005_auto_20210606_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
