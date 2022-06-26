from django.db import models
from datetime import datetime,timedelta
#from django.contrib.auth.models import User
#import datetime
#from django.db.models.signals import post_save

# Create your models here.

# relation containg all genre of books

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField('ISBN', max_length=13)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    #pic = models.ImageField(blank=True, null=True, upload_to='book_image')   


# relation containing info about student
# this helps to track students 
class Student(models.Model):
    name = models.CharField(max_length=10)
    course = models.CharField(max_length=3)
    student_no = models.PositiveIntegerField()
    contact_no = models.CharField(max_length=10)
    total_books_due = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    #pic = models.ImageField(blank=True, upload_to='profile_image')

# relation containing info about Borrowed books
# it has  foriegn key book and student for referencing book and student
# if a book is returned than corresponding tuple is deleted from database
class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.student.name + " borrowed " + self.book.title


