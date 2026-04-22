from django.contrib.auth.models import User
from django.db import models

from matches.models import Match


class IntroCall(models.Model):
    CALL_TYPE_CHOICES = [
        ("video", "Video"),
        ("audio", "Audio"),
    ]

    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
    ]

    match = models.OneToOneField(Match, on_delete=models.CASCADE, related_name="intro_call")
    scheduled_by = models.ForeignKey(User, on_delete=models.CASCADE)
    call_type = models.CharField(max_length=10, choices=CALL_TYPE_CHOICES)
    scheduled_for = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.match} - {self.call_type} on {self.scheduled_for}"