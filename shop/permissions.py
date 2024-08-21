from rest_framework import permissions

class IsInCoffeeShopReadersGroup(permissions.BasePermission):

    def has_permission(self, request, view):
        # Allow GET requests if the user is in the CoffeShopReaders group
        return request.method in permissions.SAFE_METHODS and request.user.groups.filter(name='CoffeShopReaders').exists()