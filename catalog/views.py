from gc import get_objects

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.backends.base import UpdateError
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ProductForm, ProductModeratorForm
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

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("catalog:products")

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not (request.user == product.owner) or request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас недостаточно прав для снятия продукта с публикации")
        product.delete()
        return redirect("catalog:products")

