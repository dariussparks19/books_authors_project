from django.shortcuts import render, redirect
from .models import Book, Author
# Create your views here.

#----  Books ----#
def index(request):
    context = {
        'all_books' : Book.objects.all()
    }
    return render(request, 'index.html', context)

def create_book(request):
    print(request.POST)
    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'] 
    )
    return redirect('/')

def book_id(request, book_id):
    this_book = Book.objects.get(id = book_id  )
    print(this_book)
    context = {
        "book_info" : this_book
    }
    return render(request, 'book.html', context)

# ----  Authors ----#
def authors(request):
    context = {
        "all_authors" : Author.objects.all()
    }
    return render(request, 'authors.html', context)

def create_author(request):
    print(request.POST)
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def author_id(request, author_id):
    this_author = Author.objects.get(id = author_id)
    print(this_author)
    context = {
        "author_info" : this_author,
        'all_books' : Book.objects.all()
    }
    return render(request, 'author.html', context)

def adding_book_to_author(request):
    print(request.POST)
    this_author = Author.objects.get(id = request.POST['author_id'])
    book_select = Book.objects.get(id = request.POST['book_id'])
    this_author.books.add(book_select)
    return redirect('/authors/' + request.POST['author_id'])