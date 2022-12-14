# Generated by Django 3.2.14 on 2022-07-23 01:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20220723_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literary',
            name='number',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='رقم الطالب '),
        ),
        migrations.AlterField(
            model_name='scientific',
            name='number',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='رقم الطالب '),
        ),
    ]
