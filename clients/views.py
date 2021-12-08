from django.contrib import auth
from django.shortcuts import redirect, render
from home.models import customer,Account
from django.contrib import messages

def display_menu(request):
    global cst
    for obj in customer.objects.all():
        if obj.username == request.user.username:
            cst = obj
            return render(request,'user_account.html',{'customer':obj})


def get_function_choosen(request):
    global acc
    menu_choosen = request.GET['function_chosen']
    if(menu_choosen == 'view_personal_information'):
        return render(request, 'details.html',{'customer':cst})
    elif(menu_choosen == 'deposit'):
        for obj in Account.objects.all():
            if obj.Owner == cst:
                acc = obj
        return render(request,'deposit.html', {'accounts':acc})
    elif(menu_choosen == 'withdraw'):
        for obj in Account.objects.all():
            if obj.Owner == cst:
                acc = obj
        return render(request,'withdraw.html', {'accounts':acc})
    elif(menu_choosen == 'money_transfer'):
        for obj in Account.objects.all():
            if obj.Owner == cst:
                acc = obj
        return render(request,'Transfer.html', {'accounts':acc})
    elif(menu_choosen == 'balance_enquiry'):
        for obj in Account.objects.all():
            if obj.Owner == cst:
                acc = obj
        return render(request,'balance_enquiry.html', {'accounts':acc})
    elif(menu_choosen == 'accout_modification'):
        return render(request, 'account_modification.html',{'customer':cst})
    elif(menu_choosen == 'Mobile_Balance'):
        for obj in Account.objects.all():
            if obj.Owner == cst:
                acc = obj
        return render(request,'MobileRecharge.html', {'accounts':acc})


def deposit(request):
    # global acc
    if request.method == 'POST':
        Balance = request.POST.get('amount')
        # print(Balance)
        acc.Balance += float(Balance)
        acc.save()
        messages.success(request,'Amount Deposited Successfully')
        return render(request,'deposit.html', {'accounts':acc})

def withdraw(request):
    # global acc
    # print('ahtisham')
    if request.method == 'POST':
        Balance = request.POST.get('amount')
        # print(Balance)
        acc.Balance -= float(Balance)
        if(acc.Balance < 0):
            messages.success(request,"You Don't have Required Amount To Withdraw")
            return render(request,'withdraw.html', {'accounts':acc})
        acc.save()
        messages.success(request,'Amount Withdrawn Successfully')
        return render(request,'withdraw.html', {'accounts':acc})

def transfer(request):
    if request.method == 'POST':
        Balance = request.POST.get('amount')        
        acc.Balance -= float(Balance)
        if(acc.Balance < 0):
            messages.success(request,"You Don't have Required Amount To Transfer")
            return render(request,'Transfer.html', {'accounts':acc})
        
        
        Transfer_to = request.POST.get('acc_no')

        for obj in Account.objects.all():
            # print('obj ', obj.Accno)
            # print('trans ',Transfer_to)
            if int(obj.Accno) == int(Transfer_to):
                obj.Balance += float(Balance)
                obj.save()
                acc.save()
                messages.success(request,"Amount Transferred Successfully")
                return render(request,'Transfer.html', {'accounts':acc})
        
        messages.success(request,"Account Don't Exist ")
        return render(request,'Transfer.html', {'accounts':acc})

def modification(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('phone')
        email = request.POST.get('email')   
        cnic = request.POST.get('cnic')
        if name != "":
            for obj in customer.objects.all():
                if obj.name == name:
                    messages.success(request,'Name Exists in Database Use another Name')
                    return render(request, 'account_modification.html',{'customer':cst})
            cst.name = name
        if number != "":
            for obj in customer.objects.all():
                if obj.phone == number:
                    messages.success(request,'Number Exists in Database Use another Number')
                    return render(request, 'account_modification.html',{'customer':cst})
            cst.phone = number
        if email != "":
            for obj in customer.objects.all():
                if obj.email == email:
                    messages.success(request,'Email Exists in Database Use another Email')
                    return render(request, 'account_modification.html',{'customer':cst})
            cst.email = email
        if cnic != "":
            for obj in customer.objects.all():
                if obj.cnic == cnic:
                    messages.success(request,'CNIC Exists in Database Use another CNIC')
                    return render(request, 'account_modification.html',{'customer':cst})
            cst.cnic = cnic
        cst.save()
        messages.success(request,'Account Info modified Successfully')
        return render(request, 'account_modification.html',{'customer':cst})

def recharge(request):

    if request.method == 'POST':
        Balance = request.POST.get('amount')
        # print(Balance)
        acc.Balance -= float(Balance)
        if(acc.Balance < 0):
            messages.success(request,"You Don't have Required Amount To Recharge")
            return render(request,'MobileRecharge.html', {'accounts':acc})
        acc.save()
        messages.success(request,'Recharged Successfully')
        return render(request,'MobileRecharge.html', {'accounts':acc})
        