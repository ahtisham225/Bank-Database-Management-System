from django.contrib import admin
from django.urls import path, include
from clients import views

app_name = "clients"
urlpatterns = [
    path(r"dashboard",views.display_menu,name= 'dashboard'),
    path(r"get_function_choosen", views.get_function_choosen,name='Function'),
    path(r"deposit",views.deposit,name="Deposit"),
    path(r"withdraw",views.withdraw,name="Withdraw"),
    path(r"transfer",views.transfer,name="transfer"),
    path(r"modification",views.modification,name="modification"),
    path(r"recharge",views.recharge,name="recharge")
    
    
]