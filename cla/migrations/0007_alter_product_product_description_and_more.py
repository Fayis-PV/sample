# Generated by Django 4.0.6 on 2022-07-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cla', '0006_product_product_description_product_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(),
        ),
    ]