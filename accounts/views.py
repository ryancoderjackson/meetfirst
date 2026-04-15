from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm


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