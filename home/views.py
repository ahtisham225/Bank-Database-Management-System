from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home.models import Contact, customer, Account
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm
from django.urls import path, include
from django.contrib.auth import authenticate
import random
import string

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
        if request.POST.get('username') == 'admin':
            messages.success(request,"Can't login to Admin Dashboard Here!")
            form = AuthenticationForm()
            return render(request, "signin.html",{"form":form})
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
        # for i in range(10000):
        #     temp = string.ascii_letters
        #     username = (''.join(random.choice(temp) for i in range(10)))
        #     temp_pass = string.digits
        #     password = (''.join(random.choice(temp) for i in range(10)))
        #     # print('password before ', password)
        #     password = password + (''.join(random.choice(temp_pass) for i in range(5)))
        #     cnic = 0
        #     phone = 0
            
        #     temp_name = string.ascii_uppercase
        #     name = (''.join(random.choice(temp_name) for i in range(10)))
        #     # print('Username : ',username)
        #     # print('Password : ',password)
        #     # print('Email : ',email)
        #     x = True
        #     while x:
        #         temp = string.ascii_letters
        #         username = (''.join(random.choice(temp) for i in range(10)))
        #         x = False
        #         for objects in User.objects.all():
        #             if objects.username == username:
        #                 x = True
        #                 break
        #     x = True
        #     while x:
        #         cnic = random.randint(100000000000000,9999999999999999)
        #         x = False
        #         for obj in customer.objects.all():
        #             if(cnic == obj.cnic):
        #                 x = True
        #                 break
        #     x = True
        #     while x:
        #         phone = random.randint(10000000000,99999999999)
        #         x = False
        #         for obj in customer.objects.all():
        #             if(phone == obj.phone):
        #                 x = True
        #                 break
        #     email = username + '@gmail.com'
        #     print('Username : ',username)
        #     print('Password : ',password)
        #     print('Email : ',email)
        #     print('phone : ',phone)
        #     print('cnic : ',cnic)
        #     form = User.objects.create_user(username,'',password)
        #     client = customer(name=name, email=email, cnic = cnic, phone = phone, username = username)
        #     x = True
        #     while x:
        #         a = random.randint(10000,100000)
        #         x = False
        #         for obj in Account.objects.all():
        #             if(a == obj.Accno):
        #                 x = True
        #                 break
        #     account = Account(Accno = a, Owner = client, Balance=random.randint(500,10000000))
        #     form.save()
        #     client.save()
        #     account.save()
        
        
        # x = True
        # while x:
        #     temp_phone = string.digits
        #     phone =(''.join(random.choice(temp_phone) for i in range(11))) 
        #     x = False
        #     for objects in customer.objects.all():
        #         if objects.phone == phone:
        #             x = True
        # x = True
        # while x:
        #     temp_phone = string.digits
        #     phone =(''.join(random.choice(temp_phone) for i in range(11))) 
        #     x = False
        #     for objects in customer.objects.all():
        #         if objects.phone == phone:
        #             x = True
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
                x = False
                for obj in Account.objects.all():
                    if(a == obj.Accno):
                        x = True
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
    