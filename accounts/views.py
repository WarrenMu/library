from django.shortcuts import render,redirect
# from .models import Student,Department 
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


def indexView(request):
    return render(request,'index.html')



def logout(request):
    auth.logout(request)
    messages.success(request,'Logout successful')
    return redirect('home')


def Page_Login(request):
    if request.method== "POST":
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username,password=password)

      if user is not None:
        auth.login(request, user)
        return redirect('home')
      else:
        messages.info(request, 'Inavlid Credentials')
        return redirect('login_url')
    else:
      return render(request,'registration/login.html')

def registerView(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register_url')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register_url')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login_url')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register_url')
  else:
    return render(request, 'registration/register.html')
