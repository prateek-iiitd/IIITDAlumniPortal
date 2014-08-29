__author__ = 'Prateek'
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def directory(request):
    return render(request, 'directory.html')