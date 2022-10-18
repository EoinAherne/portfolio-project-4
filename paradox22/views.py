from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.



def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()


    context = {'orders' :orders, 'customers':customers,
    'total_orders': total_orders, 'delivered':delivered, 'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return HttpResponse('accounts/products.html', {'products': products})

def customer(request, pk):

    customer = Customer.objects.get(id=pk)
    return HttpResponse('accounts/customer.html')


