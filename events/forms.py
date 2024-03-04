from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "text", "event_date", "place", "url", "price", "nr_tickets")

        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

        labels = {
            "title": "Título",
            "text": "Descrição",
            "event_date": "Data",
            "place": "Lugar",
            "url": "Link",
            "price": "Valor (R$)",
            "nr_tickets": "Número de ingressos disponíveis",
        }
