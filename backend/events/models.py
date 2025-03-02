from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('organizer', 'Organizer'),
        ('attendee', 'Attendee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='attendee')

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ("Upcoming", "Upcoming"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed")
    ])
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='event_posters/', null=True, blank=True)

class Registration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
