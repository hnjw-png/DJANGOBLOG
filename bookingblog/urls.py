from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"), name="blog-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('bookingSubmit', views.bookingSubmit, name='bookingSubmit'),
    path('Reservation', views.Reservation, name='Reservation'),
]
