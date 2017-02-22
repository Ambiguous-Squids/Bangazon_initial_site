from django.contrib import admin
from initial_site import models

@admin.register(models.Customer, models.ProductType, models.Product, models.PaymentType, models.Order)

class CustomerAdmin(admin.ModelAdmin):
    pass

class ProductTypeAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class PaymentTypeAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass