# Generated by Django 3.2.14 on 2022-07-22 23:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_choicesub_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicesub',
            name='number',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='رقم الطالب '),
        ),
    ]
