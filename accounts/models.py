from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    preferred_call_type = models.CharField(
        max_length=10,
        choices=[
            ('video', 'Video'),
            ('audio', 'Audio'),
        ],
        default='video'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username