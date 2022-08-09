# Generated by Django 3.2.14 on 2022-07-23 01:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20220723_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choiceliterary',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='رقم الطالب '),
        ),
        migrations.AlterField(
            model_name='choicescientific',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='رقم الطالب '),
        ),
    ]
