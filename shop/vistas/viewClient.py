from shop.models import Client  # Asegúrate de que el nombre sea correcto
from rest_framework import viewsets, permissions
from shop.serializers.serializersClient import ClientSerializers



class ClientViewSets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = ClientSerializers