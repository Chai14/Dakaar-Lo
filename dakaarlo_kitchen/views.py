from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from Services.models import Chinese,Italian,Indian_Street,North,South,Guj, Custom
from django.contrib.auth.models import User
from django.contrib import messages
from Services.forms import CustomSection

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
        email = request.POST['email']

        myuser = User.objects.create_user(username, email)
        myuser.name = username
        myuser.save()

        messages.success(request, "Lets start cooking for you!😈")

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



