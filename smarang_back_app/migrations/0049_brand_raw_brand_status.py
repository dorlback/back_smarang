# Generated by Django 4.1 on 2023-02-09 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smarang_back_app', '0048_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand_raw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=50, null=True)),
                ('brand_addr', models.CharField(max_length=50)),
                ('brand_date', models.CharField(max_length=50)),
                ('brand_scale', models.CharField(max_length=50)),
                ('brand_shape', models.CharField(max_length=50)),
                ('brand_price', models.CharField(max_length=50)),
                ('brand_profit', models.CharField(max_length=50)),
                ('brand_profit_loss', models.CharField(max_length=50)),
                ('brand_credit_grade', models.CharField(max_length=50)),
                ('brand_credit_grade_score', models.CharField(max_length=50)),
                ('brand_employees', models.CharField(max_length=50)),
                ('brand_industry', models.CharField(max_length=50)),
                ('brand_Needs', models.CharField(max_length=50)),
                ('brand_grade', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ver_id', models.IntegerField(default=-1)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_id', to='smarang_back_app.brand_raw')),
            ],
        ),
    ]
