from django.db import models


# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    
    def __str__(self):
        return self.name



#Product model
class Product(models.Model):
    CATEGORY = (
        ('Collection', 'Collection'),
        ('Delivery', 'Delivery'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)      

#Order Model
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery','Out for delivery' ),
        ('Delivered', 'Delivered'),
    )

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)