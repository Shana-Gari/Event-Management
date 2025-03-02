from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer, CustomUserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny


User = get_user_model()

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  # Allow public user registration

class EventViewSet(viewsets.ModelViewSet):
    # queryset = Event.objects.all()
    queryset = Event.objects.filter(status="Upcoming") 
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # Public read, only logged-in users can create/update

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)  # Automatically assign creator

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  # Only logged-in users can register

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign authenticated user