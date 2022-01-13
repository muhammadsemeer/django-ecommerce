from django.contrib import admin
from authentication.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser',
                    'is_active', 'is_staff')


# Register your models here.
admin.site.register(User, AdminUser)
