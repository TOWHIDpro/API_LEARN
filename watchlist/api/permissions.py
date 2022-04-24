from ast import Or
from rest_framework import permissions

class AdminOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        admin_permition = bool(request.user.is_staff)
        x = False
        print(x)
        if x == True:
            x = False
            print('ok')
            return x
        else:
            x = True
            print('ok5')
            return x
        
        