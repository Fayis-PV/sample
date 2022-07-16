from django.shortcuts import render
from .models import Product

# Create your views here.

def index(req):
    # product_list = Product.objects.all()
    # context = {
    #     product_list: 'product_list'
    # }
    return render(req,'index.html')

def about(req):
    return render(req,'about.html')

def computer(req):
    return render(req,'computer.html')

def laptop(req):
    return render(req,'laptop.html')

def product(req):
    return render(req,'product.html')

def contact(req):
    return render(req,'contact.html')