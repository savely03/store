# Generated by Django 4.1.3 on 2022-12-08 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0004_alter_confirmorder_пользователь_alter_order_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="confirmorder", name="Пользователь",),
        migrations.AddField(
            model_name="confirmorder",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
            preserve_default=False,
        ),
    ]
