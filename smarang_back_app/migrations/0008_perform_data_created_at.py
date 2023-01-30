# Generated by Django 4.1 on 2023-01-13 08:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0007_remove_perform_data_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='perform_data',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]