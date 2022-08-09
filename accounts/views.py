from email.message import EmailMessage
import smtplib
from django.contrib import messages
from cla.views import is_json
from cla.models import *
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def login(req):
    if is_json(req):
        return redirect('/')
    if req.method =='POST':
        username = req.POST['username']
        password = req.POST['password']
        # print(username,password)

        user = auth.authenticate(username = username, password = password)
        if user :
            auth.login(req,user)
            return redirect('/')
        else:
            messages.info(req,'Invalid Credentials!....')
            # return render(req,'login.html')

    return render(req,'login.html')

def register(req):
    if is_json(req):
        return redirect('/login')
    if req.method == 'POST':
        first_name =  req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        confirm_password =req.POST['confirm_password']
        if email == User.objects.check(email=email):
            messages.info(req,'User Name  Already Taken!...')
        elif username == User.objects.check(username=username):
            messages.info(req,'Email  Already Taken!...')
        elif password != confirm_password:
            messages.info(req,'PLS confirm password correctly!...')
        else:
            user = User.objects.create_user(first_name = first_name,last_name = last_name,username = username,email= email,password=password)
            user.save()
            user_id = user.id
            print(user_id)
            customer = Customer.objects.create(user_id = user_id,first_name = first_name,last_name = last_name,username = username,email= email,password=password)
            customer.save()
            return redirect('/register/login')
    return render(req,'register.html')

def logout(req):
    auth.logout(req)
    return redirect('/')

def subscribe(req):
    if User.is_authenticated:
        if req.method == 'POST':
            if req.POST['subscribe_email']:
                subscribe_email = req.POST['subscribe_email']
            else:
                print()
                username = req.user
                print(username)

                subscribe_email = User.objects.get(username = username).email
                # subscribe_email= User.objects.get(email = email)
            
            sender = 'mfpvcode@gmail.com'
            password = 'frmnhzjocwibfyik'
            receiver = subscribe_email
            server = smtplib.SMTP_SSL('smtp.gmail.com',465)
            msg = EmailMessage()
            msg['Subject'] = 'Mail from CLA Website'
            msg['From'] = sender
            msg['To'] = receiver
            msg.set_content = '"Thank you for Subscribtion"'
            # msg.set_content = 'Thank you for Subscribtion our website \n\n\n Thankfully, \n Team CLA'
            
            server.login(user=sender,password=password)
            server.send_message(msg)
            print(msg)



    else:
        redirect('/login')
        
    
    return render(req,'index.html')