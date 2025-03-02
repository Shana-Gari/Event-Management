from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer
from .permissions import IsOwnerOrReadOnly  # Import the custom permission

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # Apply custom permission

    def perform_create(self, serializer):
        # Ensure the logged-in user is set as the event creator
        serializer.save(created_by=self.request.user)

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
