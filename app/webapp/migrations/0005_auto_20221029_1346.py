# Generated by Django 3.2 on 2022-10-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AN', 'Разное'), ('CP', 'Компьютеры'), ('SM', 'Смартфоны'), ('CL', 'Одежда')], default='AN', max_length=2, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/images/empty.jpg', null=True, upload_to='media/images', verbose_name='Изображение'),
        ),
    ]
