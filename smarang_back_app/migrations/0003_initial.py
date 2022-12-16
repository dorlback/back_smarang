# Generated by Django 4.1 on 2022-12-15 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('smarang_back_app', '0002_delete_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
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
        ),
        migrations.CreateModel(
            name='Marketer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketer_age', models.CharField(max_length=50)),
                ('marketer_addr', models.CharField(max_length=50)),
                ('marketer_job', models.CharField(max_length=50)),
                ('marketer_career', models.CharField(max_length=50)),
                ('marketer_form', models.CharField(max_length=50)),
                ('marketer_plat', models.CharField(max_length=50)),
                ('marketer_pow', models.CharField(max_length=50)),
                ('marketer_grade', models.CharField(max_length=50)),
            ],
        ),
    ]
