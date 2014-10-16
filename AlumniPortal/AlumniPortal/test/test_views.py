from django.shortcuts import render
from AlumniPortal.forms import DirectoryForm

__author__ = 'ankur'
from django.http import HttpResponse, HttpResponseBadRequest

def hello(request):
    return HttpResponse()

def form_test(request):

    if request.method=='POST':
        form = DirectoryForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("Thanks")

    form = DirectoryForm()
    return render(request, 'form_test.html', {'form': form})