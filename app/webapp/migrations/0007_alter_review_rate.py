# Generated by Django 3.2 on 2022-10-29 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='Оценка'),
        ),
    ]