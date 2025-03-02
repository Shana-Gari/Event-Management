from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Event, Registration

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')  # Display relevant fields
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),  # Add the role field to the form
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),  # Add the role field when adding a user
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event)
admin.site.register(Registration)
