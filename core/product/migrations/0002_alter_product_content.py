# Generated by Django 4.2.2 on 2023-06-09 07:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]