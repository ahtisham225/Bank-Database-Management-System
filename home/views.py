from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Contact, customer
from django.contrib import messages
from django.contrib.auth.models import User


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


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email, password)
        # print(customer.objects.all())
        if email == '' or password == '':
            messages.success(request,'Please input in All Fields!!!')
            return render(request, "login.html")
        for obj in customer.objects.all():
            # print(obj.email)
            if obj.email == email:
                # print(obj.password)
                if obj.password == password:
                    messages.success(request,'You are loggedIn Successfully')
                    return render(request, "index.html")
                else:
                    messages.success(request,'Your Email/Password is Incorrect Try Again!')
                    break
        messages.success(request,'Your Email/Password is Incorrect Try Again!')
                    
        return render(request, "login.html")
    

    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # print(type(name))
        cnic = request.POST.get('cnic')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if name == '' or email == '' or cnic == '' or phone == '' or password == '':
            messages.success(request,'Please input in All Fields!!!')
            return render(request, "signup.html")

        client = customer(name=name, email=email, cnic = cnic, phone = phone, password = password)
        client.save()
        messages.success(request, 'Your Have Successfully Signed UP now Login To your Profile')
        return render(request, "login.html")
    


    return render(request, "signup.html")
