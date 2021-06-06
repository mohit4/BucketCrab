# Generated by Django 3.2.3 on 2021-06-05 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0002_bucket_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='Summary of the task', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(help_text='Enter details of check list item', max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklistitems', to='buckets.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(help_text='Enter details of the activities performed')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='buckets.task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
