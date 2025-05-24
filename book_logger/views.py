from django.shortcuts import render
from django.http import HttpResponse
from .form import BookForm

def home(request):
    return render(request,"book_logger/home.html")

def add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            review = form.cleaned_data["review"]
            rating = form.cleaned_data["rating"]
            return HttpResponse("The form is working good")
    form = BookForm()
    return render(request,"book_logger/add.html",{'form':form})

def about(request):
    return render(request,"")
