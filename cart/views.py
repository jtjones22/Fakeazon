from django.shortcuts import render

# Create your views here.

def view_cart(request):
    context = {}
    return render(request, 'carts/view_cart.html', context)