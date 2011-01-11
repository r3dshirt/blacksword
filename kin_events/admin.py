from kin_events.models import Event
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Published', {'fields': ['pub_date']}),
        ('Title', {'fields': ['title']}),
        ('Event Details', {'fields': ['date','location', 'players']}),
        (None, {'fields':['notes']}),
    ]

admin.site.register(Event, EventAdmin)