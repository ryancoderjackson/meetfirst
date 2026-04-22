from django.contrib.auth.models import User
from django.db import models

from matches.models import Match


class Message(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.sender.username}: {self.body[:30]}"