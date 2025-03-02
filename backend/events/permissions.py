from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to allow only the creator to edit or delete an event.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions (GET, HEAD, OPTIONS) are allowed for everyone
        if request.method in SAFE_METHODS:
            return True
        # Write permissions (PUT, DELETE) are allowed only if the user is the creator
        return obj.created_by == request.user
