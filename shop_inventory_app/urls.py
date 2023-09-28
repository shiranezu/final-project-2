from django.urls import path
from . import views

urlpatterns = [
    path('view_items/', views.item_list, name='item_list'),
    path('add_item/', views.add_item, name='add_item'),
    path('create_transaction/', views.create_transaction, name='create_transaction'),
    path('transaction_list/', views.transaction_list, name='transaction_list'),
    path('', views.Home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
