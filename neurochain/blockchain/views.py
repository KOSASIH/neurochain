from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created successfully')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})
