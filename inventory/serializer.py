from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class WarehouseSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Warehouse
		fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
	class Meta: 
		model = InventoryItem
		fields = '__all__'
