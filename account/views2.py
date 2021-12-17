from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import subscriber_required, publisher_required

def home(request):    
    render(request, 'home.html')
    
@login_required 
@subscriber_required    
def viewData(request):    
    render(request, 'viewData.html')
    
@login_required 
@publisher_required    
def publisherEdit(request):    
    render(request, 'publish.html')
    
   
def login_user(request):
    if request.method=='POST':
        email=request.POST['email']
        phone=request.post['phone']
        user = authenticate(request, email = email, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('viewData')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request, "login.html")
    
