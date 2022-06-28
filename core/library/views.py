from django.shortcuts import render, redirect
from .models import Book, Author, Isssue, Fine
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
