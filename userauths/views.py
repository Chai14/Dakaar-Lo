from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        myuser = User.objects.filter(username = username)

        if myuser.exists():
            messages.warning(request, 'User already exists')

        # if User.objects.filter(username=username).exists():
        #     messages.error(request, "Username already exist! Please try some other username.")
        #     return redirect('register')
        
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email Already Registered!!")
        #     return redirect('register')
        
        # if len(username)>20:
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('register')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return HttpResponseRedirect(request.path_info)
        
        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!!")
        #     return redirect('register')


        myuser = User.objects.create_user(username = username, email = email, password1 = password1)
        # myuser.username = username
        myuser.set_password(password1)
        # myuser.is_active = False
        myuser.save()
        messages.success(request, "An email has been sent on your email!")
        # messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        
        # messages.success(request, "Account Created!")

        return HttpResponseRedirect(request.path_info)
    
    return render(request, "register.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(request, username=username, password1=password1)

        if user is not None:
            login(request, user)
            return render(request, 'menu.html',{"username":username})
        else:
            messages.error(request, "Try Again")
            return redirect('home')

    return render(request, "signup.html")

