from django.db import models


class Language(models.Model):

    name = models.CharField(max_length=32)
    good = models.BooleanField(null=True)

    def get_form(self):
        from main.forms import LanguageForm
        return LanguageForm(instance=self)
