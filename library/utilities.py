import datetime
from django.utils import timezone
from .models import Book
from accounts.models import Student

    
def getmybooks(user):
    "Get issued books or requested books of a student, takes a user & returns a tuple "
    requestedbooks=[]
    issuedbooks=[]
    if user.is_authenticated:
        student = Student.objects.filter(student_id=user)
        if student:
            for b in Book.objects.all():
                for i in b.issue_set.all():
                    if i.student==student[0]:
                        if i.issued:
                            issuedbooks.append(b)
                        else:
                            requestedbooks.append(b)
    return [requestedbooks,issuedbooks]