# Generated by Django 4.1 on 2023-01-16 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0012_remove_authsms_auth_pass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_succ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userstate', models.BooleanField(default=False)),
                ('Item_title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='Brand_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Brand_user_id', to='smarang_back_app.brand_user'),
            preserve_default=False,
        ),
    ]