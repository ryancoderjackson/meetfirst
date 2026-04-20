from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from accounts.models import Profile
from .models import Like


@login_required
@require_POST
def send_like(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    if profile.user != request.user:
        Like.objects.get_or_create(
            from_user=request.user,
            to_user=profile.user,
        )

    return redirect("accounts:browse_profiles")