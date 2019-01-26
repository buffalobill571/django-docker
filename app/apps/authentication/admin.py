from django.contrib import admin
from apps.authentication.forms import UserChangeForm, UserCreationForm
from apps.authentication.models import User

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    search_fields = ('email', 'first_name', 'last_name')

    list_display = ('id', 'email', 'phone')
    list_filter = ('is_admin',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Change password', {'fields': ('password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_superuser', 'is_admin')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
