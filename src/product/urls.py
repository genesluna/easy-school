from django.urls import path

from src.product.views import CreateProductView, ListProductsView


urlpatterns = [
    path("", ListProductsView.as_view(), name="list_products"),
    path("create/", CreateProductView.as_view(), name="create_product"),
]

app_name = "product"
