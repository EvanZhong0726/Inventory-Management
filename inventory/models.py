from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Warehouse(models.Model):
    id = models.AutoField(primary_key = True, editable = False)
    city = models.CharField(max_length = 50, blank = False)
    state = models.CharField(max_length = 50, blank = False)
    capacity = models.PositiveIntegerField(blank = False)
    available_capacity = models.PositiveIntegerField(editable = False, default = 0)

    def __str__(self):
        return self.city


class InventoryItem(models.Model):
    id = models.AutoField(primary_key = True, editable = False)
    product = models.CharField(max_length = 50, blank = False)
    warehouse = models.ForeignKey(Warehouse, on_delete = models.CASCADE, blank = False, null = True)
    cost = models.DecimalField(max_digits = 7, decimal_places = 2, blank = False)
    quantity = models.PositiveIntegerField(blank = False)
     
    def __str__(self):
        return str(self.product)

