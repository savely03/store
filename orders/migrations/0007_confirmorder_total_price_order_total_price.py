# Generated by Django 4.1.3 on 2022-12-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0006_rename_paid_order_confirm_remove_confirmorder_paid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="confirmorder",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
            preserve_default=False,
        ),
    ]
