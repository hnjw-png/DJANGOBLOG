from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"), name="blog-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('booking-submit', views.bookingSubmit, name='booking.html'),
    path('Reservation', views.Reservation, name='booking.html'),
]
