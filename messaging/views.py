from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from calls.models import IntroCall
from matches.models import Match
from .forms import MessageForm


@login_required
@require_POST
def send_message(request, match_id):
    match = get_object_or_404(
        Match.objects.filter(Q(user1=request.user) | Q(user2=request.user)),
        id=match_id
    )

    intro_call = get_object_or_404(IntroCall, match=match)

    if intro_call.status != "completed":
        return redirect("matches:match_detail", match_id=match.id)

    form = MessageForm(request.POST)
    if form.is_valid():
        message = form.save(commit=False)
        message.match = match
        message.sender = request.user
        message.save()

    return redirect("matches:match_detail", match_id=match.id)