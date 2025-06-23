from gc import get_objects

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView

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


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
