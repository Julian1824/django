from django.urls import path,include
from rest_framework import routers
from .vistas.viewCoffeeShop import CoffeeShopViewSet,UserViewSet,GroupViewSet,VistaViewSet,FilterView,FilterListView, readViewSet
from .vistas.viewProducts import ProductsViewSet
from .vistas.viewClient import ClientViewSets


router = routers.DefaultRouter()


router.register(r'coffeeShop', CoffeeShopViewSet, basename='coffeeShop')
router.register(r'allCoffeeShops', VistaViewSet, basename='allCoffeeShops') 
router.register(r'readCoffeeShops', readViewSet, basename='readCoffeeShops') 
router.register(r'products', ProductsViewSet)
router.register(r'client', ClientViewSets)
router.register(r'users', UserViewSet)
router.register(r'group', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('filter/',FilterView.as_view(),name='filter'),
    path('FilterListView/',FilterListView.as_view(),name='FilterListView'),
    ]