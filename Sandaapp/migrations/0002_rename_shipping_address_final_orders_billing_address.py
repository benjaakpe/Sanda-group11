# Generated by Django 3.2.8 on 2021-10-19 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sandaapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='shipping_address_final',
            new_name='billing_address',
        ),
    ]