# Generated by Django 4.2.5 on 2023-09-18 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_remove_product_image1_remove_product_image2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color')),
                ('pricerange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.price_range')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.size')),
            ],
        ),
        migrations.CreateModel(
            name='VariantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='No images available', upload_to='photos/variant')),
                ('is_available', models.BooleanField(default=True)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.variant')),
            ],
        ),
    ]