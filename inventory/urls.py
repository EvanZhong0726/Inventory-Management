from django.urls import path
from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name = 'getAllInventories'),
    path('createInventory/', views.createInventoryItem, name = 'createInventoryItem'),
    path('updateInventory/', views.updateInventoryItem, name = 'updateInventoryItem'),
    path('deleteInventory/', views.deleteInventoryItem, name = 'deleteInventoryItem'),
    path('createWarehouse/', views.createWarehouse, name = 'createWarehouse'),
]