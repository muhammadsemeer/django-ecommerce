from rest_framework.generics import CreateAPIView, ListAPIView
from products.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from products.models import Product

# Create your views here.


class CreateProductsAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permissions_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ListProductsAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permissions_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)