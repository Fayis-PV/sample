# Generated by Django 4.0.6 on 2022-07-17 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cla', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 17, 17, 30, 44, 69249)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_number',
            field=models.BigIntegerField(),
        ),
    ]