from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('register_reservation/<int:reservation_id>/', views.register_reservation, name='register_reservation'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]