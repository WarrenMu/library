from django.urls import path
from .views import allbooks,search,addbook,deletebook,issuerequest,myissues,issue_book,return_book,requestedissues,sort
urlpatterns = [
    path('',allbooks,name='home'),
    path('search/',search),
    path('sort/',sort),
    path('addbook/',addbook),
    path('deletebook/<int:bookID>/',deletebook),
    path('request-book-issue/<int:bookID>/',issuerequest),
    path('my-issues/',myissues),
    

]