# Generated by Django 3.1.7 on 2021-03-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holy', '0013_order_place_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_place',
            name='item',
            field=models.TextField(max_length=30),
        ),
    ]