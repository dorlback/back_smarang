# Generated by Django 4.1 on 2023-01-18 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0028_button_con_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='button_con',
            name='button_state',
            field=models.CharField(default='정상', max_length=10),
        ),
    ]