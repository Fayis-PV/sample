# Generated by Django 4.0.6 on 2022-07-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cla', '0014_checkout_checkoutitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='transaction_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
