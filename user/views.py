import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from cart.models import Cart
from company.models import Product, Company
from user.forms import SignUpForm, SignInForm

# Create your views here.

def homepage(request):
    user = request.user
    products = Product.objects.all().order_by('-created')
    if user.is_authenticated and user.is_seller:
        company = Company.objects.get(owner=user)
        context = {'products': products, 'company': company}
    else:
        context = {'products': products}
    return render(request, 'user/homepage.html', context)

def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    context = {'form': form}
    return render(request, 'user/signup.html', context)

def signin(request):
    # if request.POST:
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect('homepage')
    # context = {}
    # return render(request, 'user/signin.html', context)

    user = request.user
    if user.is_authenticated:
        return redirect('homepage')
    if request.POST:
        form = SignInForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                Cart.objects.create(customer=user)
                return redirect('homepage')
    else:
        form = SignInForm()
    context = {'form': form}
    return render(request, 'user/signin.html', context)


def signout(request):
    logout(request)
    return redirect('homepage')