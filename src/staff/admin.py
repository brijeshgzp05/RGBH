from django.contrib import admin

# Register your models here.
from .models import Post, Staff

admin.site.register(Post)
admin.site.register(Staff)
