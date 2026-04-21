from django.urls import path
from . import views

app_name = "matches"

urlpatterns = [
    path("like/<int:profile_id>/", views.send_like, name="send_like"),
    path("", views.matches_list, name="matches_list"),
]