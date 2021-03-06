# Generated by Django 3.1.7 on 2021-02-27 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holy', '0004_sign_up'),
    ]

    operations = [
        migrations.CreateModel(
            name='CATEGORY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Popular_items',
        ),
        migrations.DeleteModel(
            name='SIGN_UP',
        ),
        migrations.AddField(
            model_name='new_arrival',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='holy.category'),
        ),
    ]
