# Generated by Django 3.2.13 on 2023-04-06 09:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230405_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]