from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField( max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class  Product(models.Model):
    CATEGORY = (  ('indoor','indoor'),
                ('outdoor','outdoor'),

            )

    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (  ('pending', 'pending'),
                ('delivered', 'delivered'),
                ('out for delivery', 'out for delivery')

            )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    products =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    note =  models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.products.name



