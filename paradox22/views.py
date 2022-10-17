from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.



def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    context = {'orders' :orders, 'customers':customers}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return HttpResponse('accounts/products.html', {'products': products})

def customer(request):
    return HttpResponse('accounts/customer.html')


