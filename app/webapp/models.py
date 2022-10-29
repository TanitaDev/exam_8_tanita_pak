from django.db import models


class Category(models.TextChoices):
    ANY = 'AN', 'Разное'
    COMPUTERS = 'CP', 'Компьютеры'
    SMARTPHONES = 'SM', 'Смартфоны'
    CLOTHES = 'CL', 'Одежда'


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Название товара"
    )
    category = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=Category.choices,
        default=Category.ANY
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Описание товара'
    )
    image = models.ImageField(upload_to='images', null=True)


