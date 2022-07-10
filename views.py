from django.shortcuts import render,redirect
from django.contrib import auth
# from django.contrib.auth.models import User
from django.contrib import messages

def indexView(request):
    return render(request,'index.html')

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login_url')
    else:
        return render(request, 'login.html')