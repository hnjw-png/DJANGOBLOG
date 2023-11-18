from django.contrib import admin
from django.urls import path, include
from . import views
#from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('register_reservation/<int:reservation_id>/', views.register_reservation, name='register_reservation'),
    path('update_reservation/<reservation_id>', views.update_reservation, 'update_reservation'),
    path('delete_reseration/<reservation_id>', views.delete_reservation, name='delete_resveration'),
]