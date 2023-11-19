from django.shortcuts import render , redirect
from .models import Book
from . forms import PostForm

# Create your views here.

def book_list(request):
    data = Book.objects.all
    context = {'books':data}
    
    return render (request,'books/book_list.html',context)




def book_details(request,pk):
    data = Book.objects.get(id = pk)
    context = {'books':data}
    
    return render (request,'books/book_details.html',context)


def add_book(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = PostForm()    
    return render(request,'books/new.html',{'form':form})