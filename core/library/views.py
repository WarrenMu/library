from django.shortcuts import render, redirect
from .models import Book, Author, Isssue, Fine
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.utils import timezone
import datetime
from .utilities import calcFine, getmybooks
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth
from core import settings

# Book
def allbooks(request):
    requestedbooks,issuedbooks=getmybooks(request.user)
    allbooks=Book.objects.all()
    
    return render(request,'library/home.html',{'books':allbooks,'issuedbooks':issuedbooks,'requestedbooks':requestedbooks})
