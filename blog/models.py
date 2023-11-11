from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


SERVICE_CHOICES = (
    ("w", "wedding"), 
    ("e", "exam"), 
    ("b", "birthday"), 
    ("w","work"), 
    ("u", "undecided"),
 )

TIME_CHOICES = (
    ("2pm", "3pm"),
    ("4pm", "5pm"),
    ("6pm", "7pm"),
    
 )


class Reservation(models.Model):
    HowMany = models.ForeignKey('Client', on_delete=models.CASCADE)
    place = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="undecided")
    time = models.CharField(max_length=15, choices=TIME_CHOICES, default="3pm")

class Client(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    Reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} | day: {self.place} | time: {self.time}"