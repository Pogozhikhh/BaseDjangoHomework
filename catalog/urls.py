from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import (
    ProductListView,
    ProductDetailView,
    HomeListView,
    ContactsListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductByCategoryListView,
    CategoryListView,
)

app_name = "catalog"

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsListView.as_view(), name="contacts"),
    path("products/", ProductListView.as_view(), name="products"),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path("products/create/", ProductCreateView.as_view(), name="add_product"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:category_id>/', ProductByCategoryListView.as_view(), name='products_by_category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
