# Generated by Django 4.1 on 2023-01-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0030_alter_brand_user_phonenumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='button_status',
            name='value',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
