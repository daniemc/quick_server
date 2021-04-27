from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class UnitMeasures(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    level = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)   


class Product(models.Model):
    name = models.CharField(max_length=50)
    purchase_unit_measure = models.ForeignKey(UnitMeasures, on_delete=models.CASCADE, related_name='purchase_unit_measure')
    purchase_qty = models.IntegerField()
    sale_unit_measure = models.ForeignKey(UnitMeasures, on_delete=models.CASCADE, related_name='sale_unit_measure')
    sale_qty = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vendors(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductCosts(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    cost = models.FloatField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    credit_able = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MovementTypes(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Movements(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    movement_type_id = models.ForeignKey(MovementTypes, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.FloatField()
    total_db = models.FloatField()
    total_cr = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


