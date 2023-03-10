# Generated by Django 4.1.3 on 2022-12-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0008_alter_confirmorder_total_price_alter_orderitem_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_price",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
