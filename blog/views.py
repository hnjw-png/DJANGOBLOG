from django. shortcuts import render, redirect
from django. views import generic
from .models import Post
from datetime import datetime, timedelta
from django.contrib import messages
from .models import Reservation, Table, Client
from .forms import EventForm
import login_required


def Reservation(request):
    weekdays = validWeekday(30)

    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'Post':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Please Choose the type of event!")
            return redirect('booking.html')

        request.session['day'] = day
        request.session['service'] = service

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
        'weekdays':weekdays,
        'validateWeekdays':validateWeekdays,
    })


def bookingSubmit(request):
    user = request.user
    times = [
        "2pm-12pm", "10am-2pm", "10am-2pm"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%M-%D')
    deltatime = today + timedelta(days=30)
    strdeltatime = deltatime.strftime('%Y-%M-%D')
    maxDate = strdeltatime

    return render(request, 'booking.html', {})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendees = Attendee.objects.filter(event=event)
    return render(request, 'event/event_detail.html', {'event': event, 'attendees': attendees})
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
    return render(request, 'event/event_form.html', {'form': form})
@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    Attendee.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', event_id=event.id)