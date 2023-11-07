from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("", views.bookingSubmit, name="booking.html"),
    path("", views.Reservation, name="booking.html"),
]

