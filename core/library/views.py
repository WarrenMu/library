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

def sort(request):
    sort_type=request.GET.get('sort_type')
    sort_by=request.GET.get('sort')
    requestedbooks,issuedbooks=getmybooks(request.user)
    if 'author' in sort_type:
        author_results=Author.objects.filter(name__startswith=sort_by)
        return render(request,'library/home.html',{'author_results':author_results,'issuedbooks':issuedbooks,'requestedbooks':requestedbooks,'selected':'author'})
    else:
        books_results=Book.objects.filter(name__startswith=sort_by)
        return render(request,'library/home.html',{'books_results':books_results,'issuedbooks':issuedbooks,'requestedbooks':requestedbooks,'selected':'book'})

def search(request):
    search_query=request.GET.get('search-query')
    search_by_author=request.GET.get('author')
    requestedbooks,issuedbooks=getmybooks(request.user)

    if search_by_author is not None:
        author_results=Author.objects.filter(name__icontains=search_query)
        return render(request,'library/home.html',{'author_results':author_results,'issuedbooks':issuedbooks,'requestedbooks':requestedbooks})
    else:
        books_results=Book.objects.filter(Q(name__icontains=search_query) | Q(category__icontains=search_query))
        return render(request,'library/home.html',{'books_results':books_results,'issuedbooks':issuedbooks,'requestedbooks':requestedbooks})
