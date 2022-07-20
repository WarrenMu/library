from django.urls import path

from accounts.views import registerView
from .views import allbooks,search,addbook,deletebook,issuerequest,myissues,issue_book,return_book,requestedissues,sort
#,myfines,allfines,deletefine,payfine,pay_status,

urlpatterns = [
    path('',allbooks,name='home'),
    path('search/',search),
    path('sort/',sort),
    path('addbook/',addbook),
    path('deletebook/<int:bookID>/',deletebook),
    path('request-book-issue/<int:bookID>/',issuerequest),
    path('my-issues/',myissues),
    path('all-issues/',requestedissues),
 
    path('issuebook/<int:issueID>/',issue_book),
    path('returnbook/<int:issueID>/',return_book),
  
]
