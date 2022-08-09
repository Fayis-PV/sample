import json
from django.contrib import messages
import random
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import auth


# Create your views here.

def index(req):
    count = cart_count(req)
    # customer.delete()
    # count= 0
    

    product_list = Product.objects.all()[:6]
    rand_product_list = random.sample(list(product_list), k=6)
    context = {'rand_product_list': rand_product_list,'count': count}
    return render(req, 'index.html', context)


def about(req):
    count = cart_count(req)

    return render(req, 'about.html',context={'count':count})


def computer(req):
    count = cart_count(req)
    return render(req, 'computer.html',context={'count':count})


def laptop(req):
    count = cart_count(req)
    return render(req, 'laptop.html',context={'count':count})


def product(req):
    count = cart_count(req)
    rand_product_list = Product.objects.all()
    # rand_product_list = random.sample(list(rand_product_list), k=9)
    context = {
        'rand_product_list': rand_product_list,
        'count':count
    }
    return render(req, "product.html",context)


def contact(req):
    count = cart_count(req)
    if req.method == "POST":
        print(req.POST)
        contact_name = req.POST['Name']
        contact_email = req.POST['Email']
        contact_number = req.POST['Phone Number']
        contact_message = req.POST['Message']
        contact = Contact(contact_name=contact_name, contact_email=contact_email, contact_number=contact_number,contact_message=contact_message)
        
        contact.save()
        messages.info(req, 'Thank You for your valuable message...')
    return render(req, 'contact.html',context={'count':count})


def cart(req):
    count = cart_count(req)
    if req.user.is_authenticated:
        try:
            customer = Customer.objects.get(user = req.user)
        except:
            redirect('/register/register')

        order , created = Order.objects.get_or_create(customer = customer, complete= False)
        order_items = order.orderitems_set.all()
    else:
        return redirect('/register/register')
        # order_items = []
        # order = {'get_all_total':0, 'get_items_count':0 }
    # print(order_items)
    context = {
        'order_items' : order_items,
        'order' : order,
        'count': count
    }

    return render(req, 'cart.html',context)


def checkout(req):
    count = cart_count(req)
    if req.user.is_authenticated:
        try:
            customer = Customer.objects.get(user = req.user)
        except:
            redirect('/register/register')
        order = Order.objects.get(customer = customer)
        order_items = order.orderitems_set.all()        
        checkout,created =CheckOut.objects.get_or_create(customer = customer,order=order,is_completed = False)
        print(checkout)
        checkout_items= checkout.checkoutitems_set.all()
        checkout_items.delete()

        for items in order_items:
            
            checkout_items_create = CheckOutItems.objects.create(product = items.product,checkout = checkout,quantity = items.quantity)
            checkout_items_create.save()
        checkout_items= checkout.checkoutitems_set.all()
    else:
        checkout_items = []

    context = {
        'checkout_items' : checkout_items,
        'count':count
    }
    return render(req,'checkout.html',context)

def detail(req,product_id):
    all_product = Product.objects.all()
    product = Product.objects.get(pk = product_id)
    context = {'product':product,'all_product' : all_product}
    return render(req,'detail.html',context)

def updateItem(req):
    # print(req,req.body)
    data = json.loads(req.body)
    productId = data['productId']
    action = data['action']
    # print('reloaded',productId,action)
    customer = Customer.objects.get(user = req.user)
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer = customer, complete =False)
    orderItems,created = OrderItems.objects.get_or_create(product=product,order=order)
    if action == 'add':
        orderItems.quantity += 1
    elif action == 'remove':
        orderItems.quantity -= 1
    elif action == 'delete':
        orderItems.quantity -= orderItems.quantity

    orderItems.save()
    # print(orderItems.quantity)
    Item_qty = orderItems.quantity

    if orderItems.quantity <= 0:
        
        orderItems.delete()
    cart(req)
    item_quantity = Item_qty
    all_total = order.get_all_total
    items_count = order.get_items_count

    #print(item_quantity)
    count = cart_count(req)
    data={
        'all_total' : all_total,
        'items_count':items_count,
        'item_quantity':item_quantity,
        'counts':count
    }   
    return JsonResponse(data,safe=False)


def add_to_checkout(req,product_id):
    count = cart_count(req)
    if req.user.is_authenticated:
        customer = Customer.objects.get(user = req.user)
        product = Product.objects.get(pk = product_id)
        order = Order.objects.get(customer = customer)

        order_items = OrderItems.objects.get(product=product,order = order)    
    
    else:
        checkout_items = []
        order_items = []


    if req.method=='POST':
        quantity = req.POST['quantity']
        order_items.quantity = quantity

    checkout = CheckOut.objects.get(customer = customer,order = order)
    checkout_items = checkout.checkoutitems_set.all()
    checkout_items.delete()

    checkout_item_create = CheckOutItems.objects.create(product = order_items.product,checkout=checkout,quantity = quantity)
    checkout_item_create.save()
    checkout_items = checkout.checkoutitems_set.all()
    print(checkout_items)
        
    context = {
        'count':count,
        'checkout_items':checkout_items
    }
    return render(req,'checkout.html',context)


def cart_count(req):
    if req.user.is_authenticated:
        try:
            customer = Customer.objects.get(user = req.user)
            order,create = Order.objects.get_or_create(customer=customer,complete =False)
            count= order.get_items_count
        except:
            count = 0
            
    else:
        count = 0
    return count

def is_json(req):
    try:
        json.loads(req)
    except:
        return False
    return True