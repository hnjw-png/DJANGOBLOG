from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('register_reservation/<int:reservation_id>/', views.register_reservation, name='register_rservation'),
]