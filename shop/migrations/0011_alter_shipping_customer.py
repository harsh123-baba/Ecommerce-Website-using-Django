# Generated by Django 3.2.5 on 2021-07-06 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.customer'),
        ),
    ]