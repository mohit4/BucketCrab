# Generated by Django 3.2.3 on 2021-06-03 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='Name of the bucket', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Few words about the bucket', null=True)),
                ('is_open', models.BooleanField(default=True)),
                ('is_expirable', models.BooleanField(default=False)),
                ('expiration_date', models.DateTimeField(blank=True, help_text='Bucket will be automatically closed on this date', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]