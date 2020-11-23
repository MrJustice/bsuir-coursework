from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Product)
admin.site.register(Order)
# admin.site.register(Order_state)