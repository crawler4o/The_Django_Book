from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book

# Create your views here.

# def search_form(request): # no longer needed
    # return render(request, 'Books/search_form.html')


def search(request):
    errors = []

    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Please enter a search criteria.')
        elif len(q)>31:
           errors.append('The search criteria cannot exceed 30 symbols.')
        else:
           books = Book.objects.filter(title__icontains=q)
           return render(request, 'books/search_results.html', {'books':books, 'book':q})
    return render(request, 'books/search_form.html', {'errors':errors})
