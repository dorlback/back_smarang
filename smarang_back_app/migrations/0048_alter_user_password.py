# Generated by Django 4.1 on 2023-02-08 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0047_alter_marketer_detail_marketer_addr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
