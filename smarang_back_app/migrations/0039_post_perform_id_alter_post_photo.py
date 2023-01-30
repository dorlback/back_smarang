# Generated by Django 4.1 on 2023-01-25 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0038_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='perform_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='perform_id_post', to='smarang_back_app.perform_data'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='post/'),
        ),
    ]