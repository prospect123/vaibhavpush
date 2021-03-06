# Generated by Django 3.1.7 on 2021-03-14 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holy', '0011_customer_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_detail',
            name='email',
            field=models.EmailField(max_length=40),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='zipcode',
            field=models.CharField(max_length=6),
        ),
        migrations.CreateModel(
            name='Order_place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holy.customer_detail')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holy.new_arrival')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
