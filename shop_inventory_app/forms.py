from django import forms
from .models import Item
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price']

class TransactionForm(forms.Form):
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.CheckboxSelectMultiple)