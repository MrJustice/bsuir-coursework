from .forms import *
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    products = Product.objects.all()[:3]
    return render(request, 'lazyhelper/home.html', {'products': products})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('validdddddd')
            form.save()
            return redirect('/login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'lazyhelper/register.html', context)

def login(request):
    
    context = {}
    return render(request, 'lazyhelper/login.html', context)

def catalog(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'lazyhelper/catalog.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'lazyhelper/product.html')

def user(request, pk):
    user = CustomUser.objects.get(id=pk)
    if user.role.role == 'Customer':
        orders = user.customer.all()
        order_count = orders.count()
        vacant = orders.filter(state='Vacant')
        inprogress = orders.filter(state='In progress')
        done = orders.filter(state='Done')
        context = {'user': user, 'orders': orders, 'order_count': order_count,
        'vacant_orders': vacant, 'inprogress_orders': inprogress, 'done_orders': done}
    elif user.role.role == 'Contractor':
        all_orders = Order.objects.filter(state='Vacant')
        orders_count = all_orders.count()
        contractor_orders = user.contractor.all()
        inprogress = contractor_orders.filter(state='In progress')
        done = contractor_orders.filter(state='Done')
        context = {'user': user, 'contractor_orders': contractor_orders, 'orders_count': orders_count,
        'inprogress_orders': inprogress, 'done_orders': done, 'all_orders': all_orders}

    return render(request, 'lazyhelper/user.html', context)

def create_order(request, pk):
    customer = CustomUser.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'lazyhelper/order_form.html', context)
    
def feedback(request):
    return render(request, 'lazyhelper/feedback.html')

def guarantees(request):
    return render(request, 'lazyhelper/guarantees.html')