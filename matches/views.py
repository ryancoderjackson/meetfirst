from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.models import Profile
from .models import Like, Match
from messaging.forms import MessageForm
from messaging.models import Message


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

            match, match_created = Match.objects.get_or_create(
                user1=user_a,
                user2=user_b
            )

            if match_created:
                messages.success(
                    request,
                    f"You matched with {profile.user.profile.display_name}!"
                )

    return redirect("accounts:browse_profiles")


@login_required
def matches_list(request):
    matches = Match.objects.filter(
        Q(user1=request.user) | Q(user2=request.user)
    ).order_by("-created_at")

    match_profiles = []
    for match in matches:
        other_user = match.user2 if match.user1 == request.user else match.user1
        match_profiles.append({
            "match": match,
            "profile": other_user.profile,
        })

    return render(request, "matches/matches_list.html", {"match_profiles": match_profiles})


@login_required
def match_detail(request, match_id):
    match = get_object_or_404(
        Match.objects.filter(Q(user1=request.user) | Q(user2=request.user)),
        id=match_id
    )

    other_user = match.user2 if match.user1 == request.user else match.user1
    other_profile = other_user.profile

    intro_call = getattr(match, "intro_call", None)
    messages = match.messages.all()

    message_form = None
    if intro_call and intro_call.status == "completed":
        message_form = MessageForm()

    return render(
        request,
        "matches/match_detail.html",
        {
            "match": match,
            "profile": other_profile,
            "intro_call": intro_call,
            "messages": messages,
            "message_form": message_form,
        }
    )