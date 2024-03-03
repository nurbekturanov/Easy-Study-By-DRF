from rest_framework import permissions


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        # if request.user.is_authenticated and request.user.is_teacher:
        #     return True
        
        if request.method in permissions.SAFE_METHODS:
            return True
    
        return False

    def has_object_permission(self, request, view, obj):
         return obj.author == request.user


class IsaAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.user.is_authenticated and request.user.is_teacher:
            return True

        # if request.user.is_authenticated and (request.user.TEACHER == request.user.role):
        #     return True
        

        if request.method in permissions.SAFE_METHODS:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always allow GET, HEAR, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a course
        return obj.author == request.user