# Generated by Django 4.1 on 2023-01-17 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0016_alter_item_succ_item_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_succ',
            name='Marketer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Marketer_user_succ', to='smarang_back_app.marketer_user', unique=True),
        ),
    ]