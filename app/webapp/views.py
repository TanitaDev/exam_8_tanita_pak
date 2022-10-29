from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'


class ProductView(DetailView):
    template_name = 'product_detail.html'
    model = Product

    def get_avg_rating(self):
        reviews = Review.objects.filter(product=self)
        count = len(reviews)
        sum = 0
        for rvw in reviews:
            sum += rvw.rating
        return (sum / count)


class ProductCreate(LoginRequiredMixin, CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDelete(LoginRequiredMixin, DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')


class ProductUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    model = Product
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ReviewCreate(LoginRequiredMixin, CreateView):
    template_name = 'review_create.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('index')
