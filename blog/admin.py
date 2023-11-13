from django.contrib import admin
from .models import reservation, client
from django_summernote.admin import SummernoteModelAdmin
admin.site.register


@admin.register(reservation)
class Reservation(admin.ModelAdmin):
    list_display = ('title', 'description', 'service', 'date', 'time', 'location')
