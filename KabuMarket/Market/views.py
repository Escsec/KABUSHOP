from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Profile, Category, Product, User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        password2 =request.POST['password2']


        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already in Use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Not Available !')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                messages.info(request,'Signup success')
                return redirect('login')
        else:
            messages.info(request, "Passwords don't Match")
            return redirect('register')
    else:
        return render(request, 'base/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)  # type: ignore
            messages.info(request, 'Succefuly logged in as ' + username )
            return redirect ('/')
        else:
            messages.info(request, 'Incorrect Username or Password')
            return redirect ('login')

    else:
        return render(request, 'base/login.html')
    

    
def logout(request):
    auth.logout(request)
    messages.info(request,'Log out success')
    return redirect('/')
   

@login_required(login_url='login')
def profile(request, pk):
    profiles = Profile.objects.all()
    profiles = Profile.objects.filter(id=pk)
    context = {'profiles': profiles}
    return render(request, 'base/profile.html', context)

def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    product_search = Product.objects.filter(
        Q(category__Category__icontains=q) |
        Q(title__icontains=q) |
        Q(description__icontains=q)
    )

    products = Product.objects.all()
    context = { 'products' : products, 'product_search' : product_search }
    return render(request, 'base/index.html', context)


@login_required(login_url='login')
def product(request, pk):
    return render(request, 'base/product.html')