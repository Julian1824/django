from shop.models import CoffeShop  # Asegúrate de que el nombre sea correcto
from rest_framework import viewsets, permissions, generics,filters
from shop.serializers.serializersCoffeeShop import CoffeeShopSerializers, UserSerializers, GroupSerializers
from django.contrib.auth.models import User, Group
from shop.permissions import IsInCoffeeShopReadersGroup

class CoffeeShopViewSet(viewsets.ModelViewSet):
    queryset = CoffeShop.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CoffeeShopSerializers  

    def get_queryset(self):
        import pdb; pdb.set_trace()
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name=name)
        return queryset
    
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
    
class VistaViewSet(viewsets.ModelViewSet):
    queryset = CoffeShop.objects.all()
    permission_classes = [permissions.IsAuthenticated|ReadOnly]
    serializer_class = CoffeeShopSerializers

    def get_queryset(self):
        
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name=name)
        return queryset

class readViewSet(viewsets.ModelViewSet):
    queryset = CoffeShop.objects.all()
    serializer_class = CoffeeShopSerializers
    permission_classes = [IsInCoffeeShopReadersGroup]


class FilterView(generics.ListAPIView):
    queryset = CoffeShop.objects.all()
    serializer_class = CoffeeShopSerializers
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name', 'direction', 'productos']

class FilterListView(generics.ListAPIView):
    queryset = CoffeShop.objects.all()
    serializer_class = CoffeeShopSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'direction']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticated]
