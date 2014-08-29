__author__ = 'Prateek'
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def directory(request):
    return render(request, 'directory.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def blog(request):
    return render(request, 'blog.html')