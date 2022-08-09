# Generated by Django 3.2.14 on 2022-07-21 19:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_choicesub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicesub',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('اللغة العربية', 'اللغة العربية'), ('الرياضيات', 'الرياضيات'), ('اللغة الانكليزية', 'اللغة الانكليزية'), ('اللغة الفرنسية', 'اللغة الفرنسية'), ('علم الاحياء', 'علم الاحياء'), ('الفيزياء', 'الفيزياء'), ('الكيمياء', 'الكيمياء'), ('التربية القومية', 'التربية القومية'), ('التربية الاسلامية', 'التربية الاسلامية')], max_length=119),
        ),
    ]
