# Generated by Django 4.0.6 on 2022-07-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cla', '0005_alter_contact_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.CharField(default='product items', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=100),
        ),
    ]
