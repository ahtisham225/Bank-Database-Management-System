from django.contrib import admin
from django.urls import path, include
from clients import views

app_name = "clients"
urlpatterns = [
    path(r"dashboard",views.display_menu,name= 'dashboard'),
    path(r"get_function_choosen", views.get_function_choosen,name='Function')
]