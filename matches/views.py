from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from accounts.models import Profile
from .models import Like, Match


@login_required
@require_POST
def send_like(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    if profile.user != request.user:
        like, created = Like.objects.get_or_create(
            from_user=request.user,
            to_user=profile.user,
        )

        mutual_like_exists = Like.objects.filter(
            from_user=profile.user,
            to_user=request.user
        ).exists()

        if mutual_like_exists:
            user_a = min(request.user, profile.user, key=lambda user: user.id)
            user_b = max(request.user, profile.user, key=lambda user: user.id)

            Match.objects.get_or_create(
                user1=user_a,
                user2=user_b
            )

    return redirect("accounts:browse_profiles")