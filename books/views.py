from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book

# Create your views here.

# def search_form(request): # no longer needed
    # return render(request, 'Books/search_form.html')


def search(request):
    try:
        if request.GET['q'] and 'q' in request.GET:
            q = request.GET['q']
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', {'books':books, 'book':q})
        elif not request.GET['q']:
            return render(request, 'books/search_form.html', {'error':True})
    except:
        return render(request, 'books/search_form.html')
