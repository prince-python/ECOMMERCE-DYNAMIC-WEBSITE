from django.shortcuts import render
from .models import *
from django.contrib import messages
def home(request):
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
    if request.method == 'POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        cpwd= request.POST['cpwd']
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already exists')
            return render(request,'app/customerregistration.html')
        elif pwd != cpwd:
            messages.error(request,'password doesnt match')
            return render(request,'app/customerregistration.html')
        else :
           u=User.objects.create(Email=email,Password=pwd)
           u.save()
           return render(request, 'app/login.html')
    else:
        return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
