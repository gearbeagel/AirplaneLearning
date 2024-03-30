from django.contrib import admin
from .models import Profile, LearnerType  # Import your Profile model


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'progress')


class LearnerTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'alternate_title', 'description')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(LearnerType, LearnerTypeAdmin)
