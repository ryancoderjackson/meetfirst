from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.profile_detail, name="profile_detail"),
    path("profile/", views.profile_detail, name="profile_detail"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]