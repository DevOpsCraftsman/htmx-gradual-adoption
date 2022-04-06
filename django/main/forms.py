from django import forms

from main.models import Language


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = [
            "name",
            "good",
        ]
