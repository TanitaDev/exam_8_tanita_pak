from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
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
    image = models.ImageField(
        upload_to='images',
        null=True
    )


class Review(models.Model):
    author = models.ForeignKey(
        to=User, related_name='review_author',
        verbose_name='Автор',
        null=False, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to=Product,
        related_name='review_product',
        verbose_name='Товар',
        null=False,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        max_length=300,
        verbose_name='Текст отзыва',
        null=False, blank=True
    )
    rate = models.FloatField(
        null=False,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
