from django.contrib import admin

from . import models


# Register your models here.
# admin.site.register(models.Event)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Ticket)


#admin.py
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date',)

admin.site.register(models.Event, EventAdmin)