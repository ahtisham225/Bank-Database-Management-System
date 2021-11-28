from django.contrib import auth
from django.shortcuts import redirect, render
from home.models import customer
def display_menu(request):
    global cst
    for obj in customer.objects.all():
        if obj.username == request.user.username:
            cst = obj
            return render(request,'user_account.html',{'customer':obj})

def get_function_choosen(request):
    print('coming here')
    menu_choosen = request.GET['function_chosen']
    if(menu_choosen == 'view_personal_information'):
        return render(request, 'details.html',{'customer':cst})    

# def view_personal_information(request):
    
