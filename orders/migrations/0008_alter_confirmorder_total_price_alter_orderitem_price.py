# Generated by Django 4.1.3 on 2022-12-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0007_confirmorder_total_price_order_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="confirmorder",
            name="total_price",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="orderitem", name="price", field=models.CharField(max_length=20),
        ),
    ]
