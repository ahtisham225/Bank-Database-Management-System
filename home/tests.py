import random
import string

from django.contrib.auth.models import User
# from django.test import TestCase
# from django.contrib.auth.models import User
# from home.models import Contact, customer, Account
# Create your tests here.

# name = request.POST.get('name')
temp = string.ascii_letters
username = (''.join(random.choice(temp) for i in range(10)))
print(username)

for obj in User.objects.all():
    if obj.username == username:
        print('hello')

# username= request.POST.get('username')
# cnic = request.POST.get('cnic')
# email = request.POST.get('email')
# phone = request.POST.get('phone')
# # print(phone)
# if name == '' or email == '' or cnic == '' or phone == '':
#     messages.success(request,'Please input in All Fields!!!')

#     form = UserCreationForm()
#     return render(request, "signup.html",{"form":form})
# for obj in customer.objects.all():
#     if obj.email == email or obj.cnic == cnic or obj.phone == phone:
#         messages.success(request,'Already Registered Phone Email or CNIC!')

#         form = UserCreationForm()
#         return render(request, "signup.html",{"form":form})

# client = customer(name=name, email=email, cnic = cnic, phone = phone, username = username)
# x = True
# while x:
#     a = random.randint(10000,100000)
#     for obj in Account.objects.all():
#         if(a == obj.Accno):
#             x = True
#             break
#     break
# account = Account(Accno = a, Owner = client, Balance=0)
# form.save()
# client.save()
# account.save()
            