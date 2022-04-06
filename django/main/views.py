from django.urls import reverse_lazy
from django.views import generic

from main.forms import LanguageForm
from main.models import Language


class LanguageView:
    model = Language
    success_url = reverse_lazy("list")
    template_name = "list.html"


class LanguageList(LanguageView, generic.ListView):
    extra_context = dict(form=LanguageForm())


class LanguageCreate(LanguageView, generic.CreateView):
    form_class = LanguageForm


class LanguageUpdate(LanguageView, generic.UpdateView):
    form_class = LanguageForm


class LanguageDelete(LanguageView, generic.DeleteView):
    get = generic.DeleteView.post
