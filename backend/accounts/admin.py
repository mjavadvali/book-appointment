from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import Userform, UserChangeForm
from .models import User

class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = Userform
    model = User
    list_display = [
                    "email",
                    "username",
                    "is_staff",
                    'type'
                ]
    readonly_fields = ('created', 'updated', 'last_login')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'created', 'updated')}),
        ('Other Info', {'fields': ('is_verified', 'type')}),
    )
    exclude = ('usable_password', 'created', 'updated')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_verified', 'type')}
         ),
    )
    

admin.site.register(User, UserAdmin)