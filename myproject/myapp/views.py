from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Review
from .forms import AuthorForm, BookForm, ReviewForm, SearchForm

def index(request):
    return render(request, 'myapp/index.html')

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()
    return render(request, 'myapp/add_author.html', {'form': form})

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)
            return render(request, 'myapp/search_results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'myapp/search.html', {'form': form})

