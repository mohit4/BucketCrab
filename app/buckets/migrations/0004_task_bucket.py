# Generated by Django 3.2.3 on 2021-06-05 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0003_activity_checklistitem_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='bucket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='buckets.bucket'),
            preserve_default=False,
        ),
    ]
