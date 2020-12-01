from django.contrib import admin

from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')

# admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Product)
admin.site.register(Order)