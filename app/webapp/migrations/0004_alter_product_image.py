# Generated by Django 3.2 on 2022-10-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/images/empty.jpg', null=True, upload_to='media/images'),
        ),
    ]
