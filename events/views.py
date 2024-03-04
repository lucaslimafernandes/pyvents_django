from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.urls import reverse

from .models import Event

from .forms import EventForm

# Create your views here.


def vw_events_list(request):
    events = Event.objects.filter(event_date__gte=timezone.now()).order_by("event_date")
    content = {"events": events}
    return render(request, "events/events_list.html", content)

def vw_new_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect(reverse('Events:vw_events_list'))

    else:
        form = EventForm()
        content = {"form": form}
        return render(request, "events/create_event.html", content)
