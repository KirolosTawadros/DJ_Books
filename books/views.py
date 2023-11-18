from django.shortcuts import render , redirect
from .models import Book

# Create your views here.

def book_list(request):
    data = Book.objects.all
    context = {'books':data}
    
    return render (request,'books/book_list.html',context)
