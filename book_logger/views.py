from django.shortcuts import render

def home(request):
    return render(request,"book_logger/home.html")

def add(request):
    return render(request,"book_logger/add.html")

def about(request):
    return render(request,"")
