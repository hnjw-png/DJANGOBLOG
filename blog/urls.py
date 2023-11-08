from django.contrib import admin
from django.urls import path, include
from blog.views import Reservation, register_reservation, reservation_detail, reservation_list, create_reservation


urlpatterns = [
    path('index/', Reservation, name='reservation'),
    path('', register_reservation, name='register_reservation'),
    path('', reservation_list, name='reservation_list'),
    path('', reservation_detail, name='reservation_detail'),    
    path('', create_reservation, name='create_reservation'),

    
]
