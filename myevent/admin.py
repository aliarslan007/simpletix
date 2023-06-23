from django.contrib import admin
from .models import Event, NewEvent, Ticket

admin.site.register(NewEvent)
admin.site.register(Ticket)
