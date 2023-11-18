from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


SERVICE_CHOICES = (
    ("w", "wedding"), 
    ("e", "exam"), 
    ("b", "birthday"), 
    ("w","work"), 
    ("u", "none of the above"),
 )

#TIME_CHOICES = (
 #   ("2pm", "2pm"),
  #  ("3pm", "3pm"),
   # ("4pm", "4pm"),
    
 # )

class Reservation(models.Model):
    title = models.CharField(max_length=200, default='Create your Reservation')
    description = models.TextField(max_length=200, default='what will you be doing?')
    service = models.TextField(max_length =100, choices=SERVICE_CHOICES, default="undecided")
    date = models.DateField(default='01:01:2024')
    time = models.TimeField(default='12:00:00')
    location = models.CharField(max_length=200, default='somewhere')
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100, blank=True)
    def __str__(self):
        return self.title

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} - {self.reservation.title}"

