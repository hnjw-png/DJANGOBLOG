from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("bookingSubmit", views.bookingSubmit, name="bookingSubmit"),
    path("Reservation", views.Reservation, name="Reservation"),
    path("", views.booking, name="booking")
]

