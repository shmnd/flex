# Generated by Django 4.2.5 on 2023-09-19 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
