customers = Customer.objects.all()

firstCustomer = Customer.objects.first()

lastCustomer = Customer.objects.last()

#Return all orders related to customer
firstCustomer.order_set.all()




 
