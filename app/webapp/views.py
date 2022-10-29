from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class ProductCreate(PermissionRequiredMixin, CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm

    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')

    permission_required = 'webapp.delete_product'


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    model = Product
    form_class = ProductForm
    context_object_name = 'product'

    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ReviewCreate(LoginRequiredMixin, CreateView):
    template_name = 'review_create.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
