from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Event, Registration

User = get_user_model()  # Fetch the custom user model before using it

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        if validated_data.get('role') == 'organizer':
            user = self.context['request'].user
            if user.role != 'admin':  # Only allow admins to create organizers
                raise serializers.ValidationError("Only admins can create organizers.")
        user = User.objects.create_user(**validated_data)
        return user

class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Registration
        fields = '__all__'
