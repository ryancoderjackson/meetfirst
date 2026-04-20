from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.profile_detail, name="profile_detail"),
    path("profile/", views.profile_detail, name="profile_detail"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("browse/", views.browse_profiles, name="browse_profiles"),
    path("profiles/<int:profile_id>/", views.public_profile_detail, name="public_profile_detail"),
]