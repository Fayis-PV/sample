# Generated by Django 4.0.5 on 2022-07-22 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cla', '0008_customer_order_orderitems_contact_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='costumer',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cla.product'),
        ),
    ]
