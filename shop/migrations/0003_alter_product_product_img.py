# Generated by Django 3.2.4 on 2021-06-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(upload_to='images/pics'),
        ),
    ]
