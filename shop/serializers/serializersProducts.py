from rest_framework import serializers
from shop.modelo.modelProducts import Products 

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name','cod_product','cant')


class ProductsViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('cod_product','name')