# Generated by Django 3.2.6 on 2021-10-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
