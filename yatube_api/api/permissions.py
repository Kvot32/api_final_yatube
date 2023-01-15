from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта, позволяющее редактировать его только владельцам объекта.
    """

    def has_object_permission(self, request, view, obj):
        # если методы безопасны, то True
        if request.method in permissions.SAFE_METHODS:
            return True

        # проверяется, является ли текущий пользователь автором
        return obj.author == request.user
