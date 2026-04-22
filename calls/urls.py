from django.urls import path
from . import views

app_name = "calls"

urlpatterns = [
    path("schedule/<int:match_id>/", views.schedule_intro_call, name="schedule_intro_call"),
]