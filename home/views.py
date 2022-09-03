from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,  login, logout
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/ulogin")
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()  
        messages.success(request, 'Feedback submitted successfully!!')
    return render(request, 'contact.html')

def uregister(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pswd=request.POST['pswd']
        cpswd=request.POST['cpswd']
        if len(username)<8:
            messages.error(request, " Username must contain 8 characters")
            return redirect('/uregister')

        if not username.isalnum():
            messages.error(request, " Username must contain letters and numbers only")
            return redirect('/uregister')
        
        if (pswd!= cpswd):
            messages.error(request, " Passwords do not match")
            return redirect('/uregister')


        myuser=User.objects.create_user(username,email,pswd)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request,'Registration Successfull!')
        return redirect('/ulogin')

    else:
        return render(request, 'uregister.html')
    
    
    
def ulogin(request):
    if request.method=="POST":
        logusername=request.POST['logusername']
        logpswd=request.POST['logpswd']
        user=authenticate(username=logusername,password=logpswd)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Invalid Username or Password!")
            return redirect("/ulogin")
    else:
        return render(request,'ulogin.html')

    
def ulogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("/ulogin")