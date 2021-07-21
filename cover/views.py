from typing import ContextManager
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from cover.models import Contact
from django.contrib import messages
import os
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_exempt


# nkn05_06
# k!Cr#F8A5rQu/Z#

# Create your views here.

def index(request):
    return redirect("/base")

def base(request):
    return render(request, 'cover/base.html')

def about(request):
    return render(request, 'cover/about.html')


def works(request): 
    return render(request, 'cover/works.html')


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, f'{name} Your form has been submitted!')
    return render(request, 'cover/contact.html')


def registerpage(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account is created for {username} !')
            return redirect("/login")
    
    else:
        form = UserRegisterForm()
    return render(request, 'cover/register.html', {'form': form})

    


    
