from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,"app/webpage1.html")
def web2(request):
    all_data=User.objects.all() 
    return render(request,"app/webpage2.html",{"data":all_data})
def RegisterUser(request):
    all_data=User.objects.all() 
    return render(request,"app/webpage2.html")
    print(all_data)
    # u=request.POST['uname']
    # e=request.POST['eml']
    # p=request.POST['passwd']
    # print(f"{uname}{em}{passwd}")

    # if u and e and p:
    #     a=User.objects.Create(username=uname,email=em,password=passwd)
    #     return redirect("webpage2")
