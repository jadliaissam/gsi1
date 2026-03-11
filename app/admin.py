# Register your models here.

from django.contrib import admin

from .models import Caracteristic, Product

admin.site.register(Product)
admin.site.register(Caracteristic)
