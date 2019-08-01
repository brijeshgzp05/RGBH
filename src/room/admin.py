from django.contrib import admin

# Register your models here.

from .models import Room, Bed

class AdminRoom(admin.ModelAdmin):
	list_display = ['roomno', 'room_type', 'fully_allocated']

admin.site.register(Room, AdminRoom)
admin.site.register(Bed)
