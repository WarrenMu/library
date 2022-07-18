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