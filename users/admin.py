from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(User)
class UserPanel (admin.ModelAdmin): 
    list_display = ['full_name','email']