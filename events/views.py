from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.urls import reverse

from .models import Event

# Create your views here.


def vw_events_list(request):

    events = Event.objects.filter(event_date__gte=timezone.now()).order_by("event_date")
    content = {'events': events}
    return render(request, 'events/events_list.html', content)

