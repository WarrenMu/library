from django.shortcuts import redirect, render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def indexview(request):
    return render(request,'index.html')

def dashboard(request): 
    return render(request,'dashboard.html')

def registerview(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = UserCreationForm
    return render(request,'registration/register.html',{'form':form})