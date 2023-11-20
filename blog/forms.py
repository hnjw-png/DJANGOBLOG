from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['title', 'description', 'service', 'date', 'time', 'location']
        