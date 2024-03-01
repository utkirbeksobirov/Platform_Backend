from django.contrib import admin
from django.conf import settings
from apps.users.models import User, Code


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active',)
    list_display_links = ('username',)
    list_editable = ('is_active',)
    list_filter = ('username', 'is_active',)


admin.site.register(User, UserAdmin)
admin.site.register(Code)