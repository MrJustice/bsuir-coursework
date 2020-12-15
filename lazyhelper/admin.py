from .forms import *
from .models import *
from django.contrib import admin

@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    model = CustomUser
    add_form = UserRegistrationForm
    form = UserChangeForm
    list_display = ('id', 'username', 'email', 'role')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')


admin.site.register(Role)
admin.site.register(Order)