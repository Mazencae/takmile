# Generated by Django 3.2.14 on 2022-07-22 23:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20220723_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicesub',
            name='number',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='رقم الطالب '),
        ),
    ]
