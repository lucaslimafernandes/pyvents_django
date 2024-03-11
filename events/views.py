from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.urls import reverse

from .models import Event, Ticket, Coupon

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
    event = get_object_or_404(Event, pk=pk)
    _tickets = Ticket.objects.filter(event=event)
    available = event.nr_tickets > _tickets.count()
    content = {"event": event, "available": available}

    return render(request, 'events/detail_event.html', content)

def vw_buy_ticket(request, pk):

    event = get_object_or_404(Event, pk=pk)
    tickets = Ticket.objects.filter(event=event)

    _available = event.nr_tickets - tickets.count()
    _ok_to_buy = True if _available > 0 else False
    content = {
        'event': event.title,
        'tickets_sold': tickets.count(),
        'available': _available,
        'ok_to_buy': _ok_to_buy
    }

    if request.method == 'POST':
    #    _user = get_user_model()
       args = {
           'owner': request.user,
           'event': event,
           'coupon': None,
       }
       tickets.create(**args)
       return HttpResponse(tickets.values_list()) 

    # return JsonResponse(content)
    return render(request, 'events/checkout.html', content)
