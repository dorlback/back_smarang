# Generated by Django 4.1 on 2023-01-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0021_cal_data_cal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cal_data',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
    ]