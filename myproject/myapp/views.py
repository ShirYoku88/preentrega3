from django.shortcuts import render
from .models import MartialArtsStudent
from .forms import MartialArtsStudentForm, SearchForm

def index(request):
    return render(request, 'myapp/index.html')

def add_student(request):
    if request.method == "POST":
        form = MartialArtsStudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MartialArtsStudentForm()
    return render(request, 'myapp/add_student.html', {'form': form})

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = MartialArtsStudent.objects.filter(name__icontains=query)
            return render(request, 'myapp/search_results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'myapp/search.html', {'form': form})
