from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from matches.models import Match
from .forms import IntroCallForm
from .models import IntroCall


@login_required
def schedule_intro_call(request, match_id):
    match = get_object_or_404(
        Match.objects.filter(Q(user1=request.user) | Q(user2=request.user)),
        id=match_id
    )

    if hasattr(match, "intro_call"):
        return redirect("matches:match_detail", match_id=match.id)

    if request.method == "POST":
        form = IntroCallForm(request.POST)
        if form.is_valid():
            intro_call = form.save(commit=False)
            intro_call.match = match
            intro_call.scheduled_by = request.user
            intro_call.save()
            return redirect("matches:match_detail", match_id=match.id)
    else:
        form = IntroCallForm()

    return render(
        request,
        "calls/schedule_intro_call.html",
        {
            "form": form,
            "match": match,
        }
    )


@login_required
@require_POST
def complete_intro_call(request, match_id):
    match = get_object_or_404(
        Match.objects.filter(Q(user1=request.user) | Q(user2=request.user)),
        id=match_id
    )

    intro_call = get_object_or_404(IntroCall, match=match)

    if intro_call.status == "scheduled":
        intro_call.status = "completed"
        intro_call.save()

    return redirect("matches:match_detail", match_id=match.id)


@login_required
@require_POST
def cancel_intro_call(request, match_id):
    match = get_object_or_404(
        Match.objects.filter(Q(user1=request.user) | Q(user2=request.user)),
        id=match_id
    )

    intro_call = get_object_or_404(IntroCall, match=match)
    intro_call.delete()

    return redirect("matches:match_detail", match_id=match.id)