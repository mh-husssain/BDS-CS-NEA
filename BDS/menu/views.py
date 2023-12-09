from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from home.models import Account

from decimal import Decimal
from .functions import validate, scrapeInflation, scrapeInterest

@login_required(login_url='/home')
def home(request):#Return HTML script
    user = request.user.email
    account = Account.objects.get(email=user)

    if request.method == "POST":
        newUsername = request.POST.get('username')
        account.username = newUsername
        try:
            picture = request.FILES['file']
            account.pfp = picture
        except:
            pass
        account.save()
        return redirect(request.path_info)
    else:
        pass
    return render(request, 'mainmenu.html')

@login_required(login_url='/home')
def balance(request):
    user = request.user.email
    account = Account.objects.get(email=user)
    inflation = scrapeInflation()
    interest = scrapeInterest()
    saving = Decimal(account.balance)*(Decimal(interest.replace("%", ""))/Decimal(100))
    saving = round(saving, 2) # 2 decimal places
    total = Decimal(account.balance + Decimal(saving))*(Decimal(100) - Decimal(inflation.replace("%", "")))/Decimal(100)
    total = round(total, 2) # 2 decimal places
    intChart = None # interestChart()

    context = {'inflation': inflation,
                'interest': interest,
                'saving': saving,
                'intChart': intChart,
                'total': total,
                }
    
    if request.method == "POST":
        balance = account.balance

        if request.POST.get("form") == 'DEPOSIT':
            # handle deposit form submission
            deposit = request.POST.get('deposit')
            valid = validate(deposit)
            if valid is True:     
                newBalance = balance + Decimal(deposit)
                account.balance = newBalance
                account.save() # Save all changes
                return redirect('/menu/balance') # Refresh
            else: # If input is not 2 d.p or integer
                messages.info(request, 'Enter a valid amount!')

        elif request.POST.get("form") == 'WITHDRAW':
            # handle withdraw form submission
            withdraw = request.POST.get('withdraw')
            valid = validate(withdraw)
            if valid is True:
                newBalance = balance - Decimal(withdraw)
                account.balance = newBalance
                account.save() # Save all changes
                return redirect('/menu/balance') # Refresh
            else: # If input is not 2 d.p or integer
                messages.info(request, 'Enter a valid amount!')
    
    return render(request, 'balance.html', context)

@login_required(login_url='/home')
def econometrics(request):
    return render(request, 'econometrics.html')

@login_required(login_url='/home')
def aboutUs(request):
    return render(request, 'aboutUs.html')


def logoutPage(request):
    logout(request)
    return redirect('/home')

