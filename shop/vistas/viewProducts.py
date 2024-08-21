from shop.models import Products  # Asegúrate de que el nombre sea correcto
from rest_framework import viewsets, permissions
from shop.serializers.serializersProducts import ProductsSerializers


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = ProductsSerializers     

    