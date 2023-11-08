from django.contrib import admin
from django.urls import path, include
from blog.views import register_reservation, reservation_detail, reservation_list, create_reservation


urlpatterns = [
    path('index/', register_reservation, name='register_reservation'),
    path('index/', reservation_list, name='reservation_list'),
    path('index/', reservation_detail, name='reservation_detail'),    
    path('index/', create_reservation, name='create_reservation'),

    
]
