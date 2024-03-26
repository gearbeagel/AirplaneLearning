from django.contrib import admin
from .models import Profile  # Import your Profile model


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'progress')  # Specify the fields you want to display


admin.site.register(Profile, ProfileAdmin)
