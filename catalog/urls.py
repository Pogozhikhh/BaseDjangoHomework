from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.home_html, name="home"),
    path("contacts/", views.contacts_html, name="contacts"),
    path("products/", views.products_html, name="products"),
    path("single_product/<int:pk>/", views.single_product_html, name="single_product")
    ] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
