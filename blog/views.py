from django. shortcuts import render, get_object_or_404, redirect
from django. views import generic
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .models import Reservation, Client
from .forms import ReservationForm

#def Reservation(request):
 #   return render(request, 'bookingblog/index.html')

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    client = Client.objects.filter(reservation=reservation)
    return render(request, 'reservation_detail.html', {'reservation': reservation, 'client': client})

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.organizer = request.user
            reservation.save()
            return redirect('reservation_detail', reservation_id=reservation.id)
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})

@login_required
def register_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    Client.objects.get_or_create(user=request.user, reservation=reservation)
    return redirect('reservation_detail', reservation_id=reservation.id)
    

@login_required
def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.delete()
    return redirect('reservation_list')


@login_required
def update_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    form = ReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
        return redirect('reservation_form', reservation_id=reservation.id)

    return render(request, 'reservation_form.html', {'reservation':reservation, 'form':form})

