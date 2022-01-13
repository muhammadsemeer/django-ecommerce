from django.urls import path
from products.views import CreateProductsAPIView, ListProductsAPIView


urlpatterns = [
    path('create', CreateProductsAPIView.as_view(), name='create_product'),
    path('', ListProductsAPIView.as_view(), name='list_product'),
]
