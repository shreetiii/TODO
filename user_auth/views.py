from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signin(request):
    if request.method == 'GET': 
        return render(request, 'login.html')
    
    else: 
        username = request.POST['username']
        password = request.POST['password']

#always create authenticate  during signins and registers

        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return redirect('home')
        else: 
            return redirect('signin')
        

def signout(request):
    logout(request)
    return redirect('signin')

def register(request):
    if request.method == 'GET': 
        return render(request, 'register.html')
    
    else: 

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname, is_superuser=False, is_staff=False)

        if user is not None:
            return  redirect('signin')
        else: 
            return redirect('register')