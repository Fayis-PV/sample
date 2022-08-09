# Generated by Django 4.0.6 on 2022-07-17 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_number', models.BigIntegerField(max_length=10)),
                ('contact_message', models.CharField(max_length=1000)),
                ('contact_date', models.DateTimeField(default=datetime.datetime(2022, 7, 17, 17, 29, 53, 845340))),
            ],
        ),
    ]