from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .models import *
from .forms import *

def index(request):
    inventoryItems = InventoryItem.objects.all()
    warehouses = Warehouse.objects.all()
    context = {'inventoryItems' : inventoryItems, 'warehouses' : warehouses}
    return render(request, "inventory/base.html", context)

def createInventoryItem(request):
    if request.method == 'POST':
        form = CreateInventory(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            cost = form.cleaned_data['cost']
            quantity = form.cleaned_data['quantity']
            warehouse = form.cleaned_data['warehouse']
            if warehouse.available_capacity >= quantity:
                inventoryItem = InventoryItem(product = product, warehouse = warehouse, cost = cost, quantity = quantity)
                inventoryItem.save()
                warehouse.available_capacity -= quantity
                warehouse.save()
                return HttpResponseRedirect("/inventory/") 
            else:
                return HttpResponseBadRequest({"no available capacity at the chosen warehouse"})
    else:
        form = CreateInventory()
        return render(request, "inventory/inventoryForm.html", {'form':form})

def createWarehouse(request):
    if request.method == 'POST':
        form = CreateWarehouse(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            capacity = form.cleaned_data['capacity']
            if not Warehouse.objects.filter(city = city):
              warehouse = Warehouse(city = city, state = state, capacity = capacity, available_capacity = capacity)
              warehouse.save()
              return HttpResponseRedirect("/inventory/")
            else:
                return HttpResponseBadRequest({"Please choose a different city"})
    else:
        form = CreateWarehouse()
        return render(request, "inventory/warehouseForm.html", {'form':form})

def updateInventoryItem(request):
    num = request.GET['id'].split("/")[0]
    inventoryItem = InventoryItem.objects.get(id = num)
    if request.method == 'POST':
        form = CreateInventory(request.POST)
        if form.is_valid():
            if inventoryItem.warehouse != form.cleaned_data['warehouse']:
                if form.cleaned_data['warehouse'].available_capacity > quantity:
                    warehouse = inventoryItem.warehouse
                    warehouse.available_capacity += inventoryItem.quantity
                    warehouse.save()
                    product = form.cleaned_data['product']
                    cost = form.cleaned_data['cost']
                    quantity = form.cleaned_data['quantity']
                    warehouse = form.cleaned_data['warehouse']
                    inventoryItem.product = product
                    inventoryItem.cost = cost
                    inventoryItem.quantity = quantity
                    inventoryItem.warehouse = warehouse
                    inventoryItem.save()
                    warehouse.available_capacity -= quantity
                    warehouse.save()
                else:
                    return HttpResponseBadRequest({"no available capacity at the chosen warehouse"}) 
            else:
                if inventoryItem.warehouse.available_capacity >= form.cleaned_data['quantity'] - inventoryItem.quantity:
                    inventoryItem.warehouse.available_capacity += inventoryItem.quantity
                    inventoryItem.warehouse.available_capacity -= form.cleaned_data['quantity']
                    inventoryItem.warehouse.save()
                    product = form.cleaned_data['product']
                    cost = form.cleaned_data['cost']
                    quantity = form.cleaned_data['quantity']
                    warehouse = form.cleaned_data['warehouse']
                    inventoryItem.product = product
                    inventoryItem.cost = cost
                    inventoryItem.quantity = quantity
                    inventoryItem.warehouse = warehouse
                    inventoryItem.save()
                else:
                    return HttpResponseBadRequest({"no available capacity at the chosen warehouse"})  
            return HttpResponseRedirect("/inventory/") 
    else:
        form = CreateInventory(initial = {'product':inventoryItem.product, 'cost': inventoryItem.cost, 'warehouse': inventoryItem.warehouse, 'quantity': inventoryItem.quantity})
        return render(request, "inventory/inventoryForm.html",{'form':form})

def deleteInventoryItem(request):
    num = request.GET['id'].split("/")[0]
    inventory = InventoryItem.objects.get(id = num)
    inventory.warehouse.available_capacity += inventory.quantity
    inventory.warehouse.save()
    inventory.delete()
    return HttpResponseRedirect("/inventory/")
    
