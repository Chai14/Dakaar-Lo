from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from Services.models import Chinese, Italian, Indian_Street, North,South, Guj, Custom, Registration
from django.contrib.auth.models import User
from django.contrib import messages
from Services.forms import CustomSection
from django.contrib.auth import authenticate, login


def homepage(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def chinese(request):
    servicedata = Chinese.objects.all()
    data = {
        'servicedata':servicedata
    }
    return render(request, "chinese.html", data)

def italian(request):
    servicedata2 = Italian.objects.all()
    data = {
        'servicedata':servicedata2
    }
    return render(request, "italian.html", data)

def indianstreet(request):
    servicedata3 = Indian_Street.objects.all()
    data = {
        'servicedata':servicedata3
    }
    return render(request, "indianstreet.html", data)

def northindian(request):
    servicedata4 = North.objects.all()
    data = {
        'servicedata':servicedata4
    }
    return render(request, "northindian.html", data)

def southindian(request):
    servicedata4 = South.objects.all()
    data = {
        'servicedata':servicedata4
    }
    return render(request, "southindian.html", data)

def gujraj(request):
    servicedata5 = Guj.objects.all()
    data = {
        'servicedata':servicedata5
    }
    return render(request, "gujrati.html", data)


def custom(request):
    return render(request, "custom.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(request, username=username, password1=password1)

        if user is not None:
            login(request, user)
            return redirect(request, 'menu.html')
        else:
            messages.error(request, "Try Again")

    return render(request, "signup.html")

def custom(request):
    if request.method == 'POST':
        form = CustomSection(request.POST)
        if form.is_valid():
            reqquest = form.cleaned_data['demo']
            emaill = form.cleaned_data['email']

            stu = Custom.objects.create(demo=reqquest, email=emaill)
            stu.save()
            return HttpResponse("Keep a watch on your mail for further details!")
    form = CustomSection() 
    return render(request, 'special_request.html', {'form': form})

def about(request):
    return render(request, "about.html")

def customercare(request):
    return render(request, "customercare.html")

def cart(request):
    return render(request, "cart.html")

def memberships(request):
    return render(request, "memberships.html")

def offers(request):
    return render(request, "offers.html")

# def register(request):
#     return render(request, "register.html")

def demo(request):
    return render(request, "demo.html")

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')


        myuser = User.objects.create_user(username, email, password1)
        myuser.username = username
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        
        messages.success(request, "Account Created!")

        return redirect('signup')
    
    return render(request, "register.html")
        
