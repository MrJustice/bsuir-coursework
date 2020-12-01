from django.shortcuts import render
from .models import *


def index(request):
    products = Product.objects.all()[:3]
    return render(request, 'lazyhelper/home.html', {'products': products})

def catalog(request):
    return render(request, 'lazyhelper/catalog.html')

def user(request, pk):
    user = User.objects.get(id=pk)
    orders = user.customer.all()
    if user.role.role == 'Customer':
        orders = user.customer.all()    
    elif user.role.role == 'Contractor':
        orders = user.contractor.all()
    order_count = orders.count()
    context = {'user': user, 'orders': orders, 'order_count': order_count}
    return render(request, 'lazyhelper/user.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'lazyhelper/product.html')

def feedback(request):
    return render(request, 'lazyhelper/feedback.html')

def guarantees(request):
    return render(request, 'lazyhelper/guarantees.html')