from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"), name="blog-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('', views.blog, name='blog'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('reservations', views.reservations, name='reseravtions'),
]
