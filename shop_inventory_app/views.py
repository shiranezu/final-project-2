from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import Item, Transaction
from .forms import ItemForm, TransactionForm, RegistrationForm
from django.contrib.auth.decorators import login_required

# item list
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

# add item
# @login_required(login_url='shop_inventory_app:login')
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

# create transaction
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['items']
            total_amount = sum(item.price for item in items)
            transaction = Transaction.objects.create(total_amount=total_amount)
            transaction.items.set(items)
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'create_transaction.html', {'form': form})

# view transaction list
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

# homepage
# @login_required(login_url='shop_inventory_app:login')
def Home(request):
    return render(request, 'welcome.html')

# register user
def register(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    return render(request, 'auth/signup.html', {'form': form})

# login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '':
            return render(request, 'auth/login.html')
        elif password == '':
            return render(request, 'auth/login.html')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'auth/login.html')





# Create your views here.
