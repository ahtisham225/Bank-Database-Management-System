from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path("",views.home,name= 'home'),
    path("about",views.about, name="about"),
    path("services", views.services, name="views"),
    path("contact",views.contact, name="contact"),
    path("faqs", views.faqs, name="faqs"),
    path("signup",views.signup, name="signup"),
    path("signin", views.signin, name="signin"),    
    path('signout',views.signout, name='signout'),
]