from rest_framework.permissions import BasePermission

class IsAdminOrOrganizer(BasePermission):
    def has_permission(self, request, view):
        # Only allow admins or organizers to create events
        if request.method == 'POST':  # Creating events
            return request.user.role == 'admin' or request.user.role == 'organizer'
        return True  # Allow GET, HEAD, and OPTIONS requests
