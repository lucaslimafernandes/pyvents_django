from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect(reverse('Events:vw_detail_event', args=[event.pk]))

    else:
        form = EventForm()
        content = {"form": form}
        return render(request, "events/create_event.html", content)

def vw_detail_event(request, pk):
    item = get_object_or_404(Event, pk=pk)
    content = {"event": item}

    return render(request, 'events/detail_event.html', content)
