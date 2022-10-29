from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'


class ProductView(DetailView):
    template_name = 'product_detail.html'
    model = Product


class ProductCreate(CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')


class ProductUpdate(UpdateView):
    template_name = 'product_update.html'
    model = Product
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})