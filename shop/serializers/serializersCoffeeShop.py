from rest_framework import serializers
from ..models import CoffeShop, Client
from django.contrib.auth.models import Group,User
from .serializersClient import ClientViewSerializers
from .serializersProducts import ProductsViewSerializers



class CoffeeShopSerializers(serializers.ModelSerializer):
    clientesConsulta = ClientViewSerializers(source='clientes', many=True, read_only=True)
    productosConsulta = ProductsViewSerializers(source='productos', many=True, read_only=True)
    class Meta:
        model = CoffeShop
        fields = ('name','direction','productos','clientes','clientesConsulta','productosConsulta')
        read_only_fields = ('',)
        extra_kwargs = {
            'productos': {'write_only': True},
            'clientes': {'write_only': True},
        }

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

