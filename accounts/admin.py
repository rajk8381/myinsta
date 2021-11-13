from django.contrib import admin

# Register your models here.
from .models import PublicUser

admin.site.register(PublicUser)