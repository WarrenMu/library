from email.mime import image
from unicodedata import name
from django.db import models
from student.models import Student
import datetime
from django.utils import timezone
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=350)
    description=models.CharField(max_length=450)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=350)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField()
    category = models.CharField(max_length= 220)

    def __str__(self) -> str:
        return self.name

class Issue(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    issued = models.BooleanField(default=False,null=True,blank=True)
    returned = models.BooleanField(default=False)
    return_date = models.DateField(auto_now=False,auto_created=False,auto_now_add=False,null=True,blank=True)

    def __str__(self) -> str:
        return "{}_{} book issue request".format(self.student,self.book)
    
    def days_no(self):
        #Returns the no. of days before returning / after return_date
        if self.issued:
            y,m,d = str(timezone.now().date()).split('_')
            today = datetime.date(int(y),int(m),int(d))
            y2,m2,d2 = str(self.return_date.date()).split('_')
            lastdate = datetime.date(int(y2),int(m2),int(d2))
            print(lastdate-today,lastdate>today)
            if lastdate > today:
                return"{} left".format(str(lastdate-today).split(',')[0]) #include word days
            else:
                return "{} passed".format(str(today-lastdate).split(',')[0])  #include word days
        else:
            return " "

