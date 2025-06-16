from gc import get_objects

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


def home_html(request):
    return render(request, "home.html")


def contacts_html(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

    return render(request, "contacts.html")


def products_html(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def single_product_html(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product" : product}
    return render(request, "single_product.html", context)
