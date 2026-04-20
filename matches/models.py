from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes_sent"
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes_received"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["from_user", "to_user"],
                name="unique_like"
            )
        ]

    def __str__(self):
        return f"{self.from_user.username} likes {self.to_user.username}"