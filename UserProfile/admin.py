from django.contrib import admin

from .models import Profile, TypeOfUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(TypeOfUser)
class TypeOfUserAdmin(admin.ModelAdmin):
    list_display = ('userType',)
