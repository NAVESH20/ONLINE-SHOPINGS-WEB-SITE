from django.shortcuts import render, redirect

from .models import product 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def addimage(request):
    return render(request,"image.html")

def image(request):
    name=request.POST.get("name")
    price=request.POST.get("price")
    Qty=request.POST.get("Qty")
    image=request.FILES.get("image")
    product.objects.create(name=name,price=price,Qty=Qty,image=image)
    return redirect(all)

def all(request):
    p=product.objects.all()
    d={"all":p}
    return render(request,"all.html",d)

def search(request):
    name=request.GET["name"]
    a=product.objects.filter(name=name)
    print(a)
    d={"all":a}
    return render(request,"all.html",d)

def update(request):
    name=request.POST.get("name")
    price=request.POST.get("price")
    Qty=request.POST.get("Qty")
    product.objects.filter(name=name).update(price=price,Qty=Qty)
    msg=f"{name}data is updated"
    return render (request,"admin.html",{"msg":msg})

def deleted(request):
    name=request.POST.get("name")
    product.objects.filter(name=name).delete()
    msg=f"{name} data is delete"
    return render (request,"admin.html",{"msg":msg})

def need(request):
    return render(request,"register.html")

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        print("username",username,"email",email,"password",password,"confirm_password",confirm_password)

        return render(request,"login.html",)
    return render(request,"register.html",)

def logins(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        User = authenticate(request,username=username, password=password)

        if User is not None:
            login(request, User)
            return redirect(all)
        else:
            return render(request,"all.html",{"Error":"Invalied username and Password"})
    return render(request,"login.html",{"Error":"Invalied username and Password"})

def user_logout(request):
    logout(request)
    return redirect(logins)