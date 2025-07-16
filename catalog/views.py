from gc import get_objects

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.backends.base import UpdateError
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ProductForm
from catalog.models import Product


class HomeListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ContactsListView(ListView):
    model = Product
    template_name = "contacts.html"


class ProductListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products")


class ProductDeleteView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("catalog:products")

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect("catalog:products")
