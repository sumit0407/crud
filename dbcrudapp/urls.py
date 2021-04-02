from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("webpage-2/",views.web2,name="webpage2"),

    #FUNCTIONALITY URL
    path("register/",views.RegisterUser,name="registeruser")
]