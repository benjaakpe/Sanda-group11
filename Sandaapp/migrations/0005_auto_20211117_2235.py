# Generated by Django 3.2.7 on 2021-11-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sandaapp', '0004_alter_customer_cust_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(max_length=5),
        ),
    ]
