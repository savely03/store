from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='products_images', verbose_name='Картинка')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='Товары',
                                 verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
