from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[("Upcoming", "Upcoming"), ("Ongoing", "Ongoing"), ("Completed", "Completed")])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
