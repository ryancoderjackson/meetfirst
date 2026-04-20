from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import ProfileForm
from .models import Profile
from matches.models import Like


@login_required
def profile_detail(request):
    profile = request.user.profile
    return render(request, "accounts/profile_detail.html", {"profile": profile})


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile_detail")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/edit_profile.html", {"form": form})


@login_required
def browse_profiles(request):
    user_profile = request.user.profile

    liked_user_ids = Like.objects.filter(
        from_user=request.user
    ).values_list("to_user_id", flat=True)

    if user_profile.interested_in == "women":
        profiles = Profile.objects.filter(gender="female").exclude(
            user=request.user
        ).exclude(
            user_id__in=liked_user_ids
        )
    elif user_profile.interested_in == "men":
        profiles = Profile.objects.filter(gender="male").exclude(
            user=request.user
        ).exclude(
            user_id__in=liked_user_ids
        )
    else:
        profiles = Profile.objects.exclude(user=request.user).exclude(
            user_id__in=liked_user_ids
        )

    return render(request, "accounts/browse_profiles.html", {"profiles": profiles})


@login_required
def public_profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    already_liked = Like.objects.filter(
        from_user=request.user,
        to_user=profile.user
    ).exists()

    return render(
        request,
        "accounts/public_profile_detail.html",
        {
            "profile": profile,
            "already_liked": already_liked,
        }
    )