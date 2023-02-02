# Generated by Django 4.1.3 on 2022-12-08 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0013_alter_confirmorder_options_alter_order_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="status",
            field=models.CharField(default=1, max_length=50, verbose_name="Статус"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="orders.confirmorder",
                verbose_name="Заказ",
            ),
        ),
    ]