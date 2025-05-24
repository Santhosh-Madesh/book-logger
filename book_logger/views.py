from django.shortcuts import render
from django.http import HttpResponse
from .form import BookForm
from .models import book

def home(request):
    data = book.objects.get(pk=1)
    data = {
        'title':data.title,
        'author':data.author,
        'review':data.review,
        'rating':data.rating,
    }
    return render(request,"book_logger/home.html",data)

def add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            review = form.cleaned_data["review"]
            rating = form.cleaned_data["rating"]
            bookobj = book(title=title,author=author,review=review,rating=rating)
            bookobj.save()
            return render(request,"book_logger/add.html",{"data":f"The book {title} has been added successfully!"})
    form = BookForm()
    return render(request,"book_logger/add.html",{'form':form})

def about(request):

    return render(request,"book_logger/about.html")
