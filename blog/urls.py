from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("bookingsubmit", views.bookingSubmit, name="bookingSubmit"),
    path("reservation", views.Reservation, name="Reservation"),
    path("test", views.Test, name="test")
]

