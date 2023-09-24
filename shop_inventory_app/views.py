from django.shortcuts import render, redirect
from .models import Item, Transaction
from .forms import ItemForm, TransactionForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

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

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})


# Create your views here.
