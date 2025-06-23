from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import (
    ProductListView,
    ProductDetailView,
    HomeListView,
    ContactsListView,
)

app_name = "catalog"

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsListView.as_view(), name="contacts"),
    path("products/", ProductListView.as_view(), name="products"),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
