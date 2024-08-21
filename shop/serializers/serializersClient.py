from rest_framework import serializers
from ..models import Client
#from .serializersCoffeeShop import CoffeeShopSerializers



class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id_number', 'name', 'lastname', 'email', 'date_birhday','create_at')
        read_only_fields = ('create_at',)


class ClientViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id_number', 'name', 'lastname')
        