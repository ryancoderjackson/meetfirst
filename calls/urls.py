from django.urls import path
from . import views

app_name = "calls"

urlpatterns = [
    path("schedule/<int:match_id>/", views.schedule_intro_call, name="schedule_intro_call"),
    path("complete/<int:match_id>/", views.complete_intro_call, name="complete_intro_call"),
]