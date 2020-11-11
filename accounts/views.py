from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

def registerPage(request):
    form = CreateUserForm()

    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
                form.save()


    context =  {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    

    total_customers = customers.count()

    total_orders = orders.count()

    pending = orders.filter( status = 'pending').count()
    delivered = orders.filter( status = 'delivered').count() 
    context = { 'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders': total_orders, 'pending': pending, 'delivered': delivered }



    
    
    return render(request, 'accounts/dashboard.html', context )

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products':products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = Order.objects.all()
    total_orders = orders.count()
    myFilter = OrderFilter (request.GET, queryset=orders)
    orders = myFilter.qs
    return render(request, 'accounts/customer.html', {'customer': customer, 'orders': orders, 'total_orders': total_orders, 'myFilter':myFilter})


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields = ('products','status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset = Order.objects.none(), instance=customer)
    #form = OrderForm(initial = {'customer':customer})
    
    if request. method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    context = {'formset':formset}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request. method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request,'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request. method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)

