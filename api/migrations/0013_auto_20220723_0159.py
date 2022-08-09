# Generated by Django 3.2.14 on 2022-07-22 22:59

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20220723_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicesub',
            name='number',
            field=models.IntegerField(verbose_name='رقم الطالب '),
        ),
        migrations.AlterField(
            model_name='choicesub',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('اللغة العربية', 'اللغة العربية'), ('الرياضيات', 'الرياضيات'), ('اللغة الانكليزية', 'اللغة الانكليزية'), ('اللغة الفرنسية', 'اللغة الفرنسية'), ('علم الاحياء', 'علم الاحياء'), ('الفيزياء', 'الفيزياء'), ('الكيمياء', 'الكيمياء'), ('التربية القومية', 'التربية القومية'), ('التربية الاسلامية', 'التربية الاسلامية')], max_length=119, verbose_name='قائمة المواد '),
        ),
    ]
