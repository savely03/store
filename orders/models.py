from django.db import models
from django.contrib.auth.models import User
from products_app.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField()
    address = models.CharField(max_length=100, verbose_name="Адрес")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    confirm = models.BooleanField(default=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Сумма')

    class Meta:
        ordering = ('created_date',)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.id} в обработке, " \
               f"Адрес доставки: {self.address}, " \
               f"Дата создания: {self.created_date}, " \
               f"Имя получателя: {self.last_name} {self.first_name}"


class ConfirmOrder(models.Model):
    STATUS_CHOICES = (
        ("Оплачен", "Оплачен"),
        ("Доставлен", "Доставлен"),
        ("Доставляется", "Доставляется"),
        ("Возврат", "Возврат"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField()
    address = models.CharField(max_length=100, verbose_name="Адрес")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="Статус", default="Оплачен")
    total_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Сумма')

    class Meta:
        ordering = ('created_date',)
        verbose_name = "Подтвержденный заказ"
        verbose_name_plural = "Подтвержденные заказы"

    def __str__(self):
        return f"Заказ №{self.id} в обработке, " \
               f"Адрес доставки: {self.address}, " \
               f"Дата создания: {self.created_date}, " \
               f"Имя получателя: {self.last_name} {self.first_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(ConfirmOrder, on_delete=models.CASCADE, verbose_name='Заказ', related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='products')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, verbose_name="Статус", default="Оплачен")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product} - Количество: {self.quantity}"
