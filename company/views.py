import re
from django.shortcuts import render, redirect
from .models import Product, Company
from .forms import CreateCompanyForm, CreateProductForm
from user.models import MyUser
from django.contrib.auth.decorators import login_required

# Create your views here.

def product(request, pk):
    product = Product.objects.get(id=pk)
    if request.user.is_authenticated and request.user.is_seller:
        company = Company.objects.get(owner=request.user)
        context = {'product': product, 'company':company}
    else:
        context = {'product': product}
    return render(request, 'products/product.html', context)

def company(request, pk):
    company = Company.objects.get(pk=pk)
    products = Product.objects.filter(company=company.id).order_by('-created')
    context = {'company': company, 'products': products}
    return render(request, 'company/company.html', context)

def create_company(request):
    form = CreateCompanyForm()
    user = request.user
    if request.method == 'POST':
        form = CreateCompanyForm(request.POST)
        if form.is_valid():
            user.is_seller = True
            user.save()
            instance = form.save(commit=False)
            instance.owner = user
            instance.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'company/create_company.html', context)


def update_company(request, pk):
    company = Company.objects.get(pk=pk)
    if request.user == company.owner:
        form = CreateCompanyForm(request.POST or None, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company', pk=pk)
        context = {'company': company, 'form': form}
        return render(request, 'company/update_company.html', context)
    else:
        return redirect('homepage')

@login_required(login_url='/signin')
def create_product(request):
    user = request.user
    if user.is_seller:
        form = CreateProductForm()
        company = Company.objects.get(owner=user)
        if request.method == 'POST':
            form = CreateProductForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.company = company
                instance.save()
                return redirect('product', pk=instance.pk)
        context = {'form': form, 'company': company}
        return render(request, 'products/create_product.html', context)
    else:
        return redirect('homepage')

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.user == product.company.owner:
        form = CreateProductForm(request.POST or None, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', pk=pk)
        context = {'product': product, 'form': form}
        return render(request, 'products/update_product.html', context)
    else:
        return redirect('homepage')