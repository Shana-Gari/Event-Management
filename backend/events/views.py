from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer, CustomUserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]  # Allow public user registration

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'organizer':  # Only allow organizers to create events
            raise PermissionDenied("You must be an organizer to create an event.")
        serializer.save(created_by=user)

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  # Only logged-in users can register

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign authenticated user
