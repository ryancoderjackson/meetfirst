from django import forms

from .models import IntroCall


class IntroCallForm(forms.ModelForm):
    scheduled_for = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = IntroCall
        fields = ["call_type", "scheduled_for"]