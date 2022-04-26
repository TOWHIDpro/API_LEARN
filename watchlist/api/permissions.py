from rest_framework import permissions

class AdminOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        admin_permition = bool(request.user.is_staff)
        return request.method == "GET" or admin_permition

class AuthorOrReadonly(permissions.BasePermission):
      def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                return request.user.id == obj.author.id



        
