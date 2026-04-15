from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "display_name",
            "age",
            "city",
            "state",
            "bio",
            "interests",
            "preferred_call_type",
        ]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
            "interests": forms.Textarea(attrs={"rows": 3}),
        }