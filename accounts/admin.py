from django.contrib import admin # type: ignore
from .models import User,UserProfile
# Register your models here.
admin.site.register(UserProfile)