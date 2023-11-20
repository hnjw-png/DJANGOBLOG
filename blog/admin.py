from django.contrib import admin
from .models import Reservation, Client
from django_summernote.admin import SummernoteModelAdmin
admin.site.register


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ('title', 'description', 'service', 'date', 'time', 'location')
