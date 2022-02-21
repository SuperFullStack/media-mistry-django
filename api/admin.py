from django.contrib import admin

# Register your models here.
from .models import Country, ProductType, Quantity, Product, Review

admin.site.register(Country)
admin.site.register(ProductType)
admin.site.register(Quantity)
admin.site.register(Product)
admin.site.register(Review)