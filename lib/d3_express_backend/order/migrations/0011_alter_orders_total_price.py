# Generated by Django 4.2.3 on 2023-08-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_orders_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
