# Generated by Django 4.2.5 on 2023-09-19 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0003_rename_name_brand_namess'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='namess',
            new_name='name',
        ),
    ]
