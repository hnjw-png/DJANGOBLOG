from django. shortcuts import render, redirect
from django. views import generic
from .models import Post
from datetime import datetime, timedelta
from django.contrib import messages


# Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def index(request):
    return render(request, "index.html", {})


def booking(request):
    weekdays = validWeekday(30)

    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'Post':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Please Choose the type of event!")
            return redirect('booking')

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

