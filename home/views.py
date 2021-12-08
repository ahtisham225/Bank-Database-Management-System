from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home.models import Contact, customer, Account
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import path, include
from django.contrib.auth import authenticate
import random
# Create your views here.

def home(request):
    
    return render(request, "index.html")

def about(request):

    return render(request, "about.html")

def services(request):

    return render(request, "services.html")

def contact(request):
    # print(request.method)
    if request.method == "POST":
        name = request.POST.get('name')
        # print(type(name))

        email = request.POST.get('email')

        message = request.POST.get('message')
        # print(message)
        if name == '' or email == '' or message == '':
            messages.success(request,'Please input in All Fields!!!')
            return render(request, "contact.html")

        contact = Contact(name=name, email=email, message = message)
        contact.save()
        messages.success(request, 'Your Message has been sent.')
    return render(request, "contact.html")

def faqs(request):
    return render(request, "faqs.html")


def signin(request):

    # print('kuch to hua ha')
    if request.method == "POST":
        User_Exists = authenticate(request, username= request.POST.get('username'), password = request.POST.get('password'))
        if User_Exists is not None:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                return redirect("clients:dashboard")
        else:
            messages.success(request,'Username or Password Invalid')
            form = AuthenticationForm()
            return render(request, "signin.html",{"form":form})
    else:
        form = AuthenticationForm()
    return render(request, "signin.html",{"form":form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            name = request.POST.get('name')
            username= request.POST.get('username')
            cnic = request.POST.get('cnic')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            # print(phone)
            if name == '' or email == '' or cnic == '' or phone == '':
                messages.success(request,'Please input in All Fields!!!')

                form = UserCreationForm()
                return render(request, "signup.html",{"form":form})
            for obj in customer.objects.all():
                if obj.email == email or obj.cnic == cnic or obj.phone == phone:
                    messages.success(request,'Already Registered Phone Email or CNIC!')

                    form = UserCreationForm()
                    return render(request, "signup.html",{"form":form})

            client = customer(name=name, email=email, cnic = cnic, phone = phone, username = username)
            x = True
            while x:
                a = random.randint(10000,100000)
                for obj in Account.objects.all():
                    if(a == obj.Accno):
                        x = True
                        break
                break
            account = Account(Accno = a, Owner = client, Balance=0)
            form.save()
            client.save()
            account.save()
            messages.success(request, 'Your Have Successfully Signed UP now Login To your Profile')
            return redirect("signin")
    else:
        form = UserCreationForm()
    return render(request,"signup.html",{"form":form})

def signout(request):
    logout(request)
    messages.success(request, 'Your Have Successfully Signed Out')
    return redirect("signin")
    