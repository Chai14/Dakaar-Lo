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

        # Check if the passwords match
        if password1 != password2:
            messages.error(request, "Passwords didn't match!")
            return HttpResponseRedirect(request.path_info)

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'User already exists')
        else:
            # Create the user and save the information
            myuser = User.objects.create_user(username=username, email=email, password=password1)
            myuser.phone = phone
            myuser.address = address
            myuser.save()

            messages.success(request, "An email has been sent to your email!")

            return HttpResponseRedirect(request.path_info)

    return render(request, "register.html")

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User credentials are valid, log in the user
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            return HttpResponseRedirect('/menu/')  # Redirect to home page or any desired URL after successful login
        else:
            # User credentials are not valid
            messages.error(request, "Invalid username or password")
            return HttpResponseRedirect(request.path_info)

    return render(request, "signup.html")

