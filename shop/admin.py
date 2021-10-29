from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Checkout)
admin.site.register(OrderItem)
admin.site.register(Customer)



