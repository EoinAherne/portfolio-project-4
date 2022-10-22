from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'delivered': delivered, 'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


# Create Order
def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        print("Printing POST: ", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

# Update view


def updateOrder(request, pk_one):

    order = Order.objects.get(id=pk_one)

    form = OrderForm(instance=order)

    if request.method == 'POST':

        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

# Delete View


def deleteOrder(request, pk_one):

    order = Order.objects.get(id=pk_one)

    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
