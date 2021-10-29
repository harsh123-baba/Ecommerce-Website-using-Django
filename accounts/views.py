from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from shop import models
import random
from django.contrib.auth.models import User
from django.contrib.auth.models import  AbstractUser
from shop.models import Customer
# Create your views here.
def register(request):
#   print(order_object)
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username= username).exists():
                messages.info(request, "UserName alreay exist")
                return redirect('/accounts/register')
            else:

                user = User.objects.create_user(username=username, password=pass1, first_name= fname, email = email, last_name = lname)
                me = User.objects.get(username=username)
                customer = Customer.objects.get_or_create(user=me, name = fname)
                user.save()  
                return redirect('/accounts/login')
        

    else:
        return render(request, 'register.html')

    
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass1']
        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials ")
            return redirect('/accounts/login')
    else:        
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')    


