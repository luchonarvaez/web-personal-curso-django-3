# Generated by Django 3.1.5 on 2021-02-02 17:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210202_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
