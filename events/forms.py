from django import forms
from django.forms import SelectDateWidget

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "text", "event_date", "place", "url", "price", "nr_tickets", "poster")

        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "event_date": SelectDateWidget(),
            "poster" : forms.TextInput(),
        }

        labels = {
            "title": "Título",
            "text": "Descrição",
            "event_date": "Data",
            "place": "Lugar",
            "url": "Link",
            "price": "Valor (R$)",
            "nr_tickets": "Número de ingressos disponíveis",
            "poster": "URL do poster",
        }

        initial = {
            "price": 0,
        }
