from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Account
from .hash import hash_bcrypt, bcryptCheck # Import hash function

# Create your views here.
def home(request):#Return HTML script
    return render(request, 'index.html')



###----Registration Page view----###
def registerPage(request):
    def verifyReg(userEmail):
        try: # ERROR HANDLING: Check if email exists
            email_exist = Account.objects.get(email=userEmail)
            return True # If exists, return True
        except Account.DoesNotExist:
            return False # Else return False
    # Endfunction verifyReg()

    if request.method == 'POST': # When server POST method (form) is submitted to server
        email = request.POST.get('email')
        password = request.POST.get('password')
        email_exist = verifyReg(email) # Check if email exists
        if email_exist is True:
            messages.info(request, 'Email exists, please use another!')
        else: # We can add the credentials to our database
            #password = hash_bcrypt(password) # Import our new hashing function
            user = Account.objects.create(email=email, username=email)
            user.set_password(password)
            user.save()
            return redirect('/home')
    else: # When GET method is submitted to server
        pass
    return render(request, 'register.html')



###----Login page view----###
def loginPage(request):
    def verifyLogin(userEmail, userPassword):
        try: # Error handling: Email does not exist?
            # Email exists in database
            # Do something with the account instance
            account = Account.objects.get(email=userEmail)
            pwCheck = account.check_password(userPassword)
            if pwCheck is True:
                return True, account
            else:
                return False, None
            '''if bcryptCheck(userPassword, account.password):
                    return True
            else:
                    return False'''
        except Account.DoesNotExist:
            # Email does not exist in database
            # Handle this case appropriately
            return False, None
    # Endfunction verifyLogin()

    if request.method == 'POST': # When POST method (form) is submitted to server
        userEmail = request.POST.get('email')
        userPassword = request.POST.get('password')
        
        verify, user = verifyLogin(userEmail, userPassword)
        if verify is True:
            #user = Account.objects.get(email=userEmail, password=userPassword)
            login(request, user)
            return redirect('/menu')
        else: # When GET method is submitted to server
            messages.info(request, 'Email or password is incorrect!')
    return render(request, 'login.html')

