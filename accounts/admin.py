from django.contrib import admin

# Register your models here.
from .models import PublicUser



class PublicUserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','gender','is_active']
admin.site.register(PublicUser, PublicUserAdmin)