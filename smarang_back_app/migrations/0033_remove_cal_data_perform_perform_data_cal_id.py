# Generated by Django 4.1 on 2023-01-24 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0032_cal_data_perform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cal_data',
            name='perform',
        ),
        migrations.AddField(
            model_name='perform_data',
            name='cal_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cal_id_perform', to='smarang_back_app.cal_table'),
            preserve_default=False,
        ),
    ]
