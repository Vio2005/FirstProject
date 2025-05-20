from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import*

# Create your views here.
def home(request):
    data=Team.objects.all()
    context={'data':data}
    return render(request,'index.html',context)

def products(request):
    data=Product.objects.all()
    context={'data':data}
    return render(request,'products.html',context)

def addproduct(request):
    product=ProductModelForm()
    if request.method=="POST":
        product=ProductModelForm(request.POST,request.FILES)
        if product.is_valid():
           
            product.save()
          
            return redirect('/products')
        else:
           
            return HttpResponse('Error')
    return render(request,'addproduct.html',{'product':product})

def team(request):
    data=Team.objects.all()
    context={'data':data}
    return render(request,'team.html',context)

def addteam(request):
    team=TeamModelForm()
    if request.method=="POST":
        team=TeamModelForm(request.POST,request.FILES)
        if team.is_valid():
           
            team.save()
          
            return redirect('/team')
        else:
           
            return HttpResponse('Error')
    return render(request,'addteam.html',{'team':team})