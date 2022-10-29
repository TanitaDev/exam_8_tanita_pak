from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator, MinLengthValidator

from .models import *


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        max_length=200, label='Заголовок',
        validators=(MinLengthValidator(limit_value=2, message='dsad'),)
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 73, 'rows': 5, 'class': ''})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise ValidationError('Длина маленькая')
        if Product.objects.filter(name=name).exists():
            raise ValidationError('уже есть')
        return name


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'product', 'text', 'rate']
        exclude = ['author']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 73, 'rows': 5, 'class': ''})
        }
