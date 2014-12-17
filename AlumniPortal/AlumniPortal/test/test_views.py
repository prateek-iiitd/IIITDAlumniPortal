from django.shortcuts import render
from AlumniPortal.forms import DirectoryForm, EventForm, NewsForm
import datetime

__author__ = 'ankur'
from django.http import HttpResponse, HttpResponseBadRequest


def hello(request):
    return HttpResponse()


def form_test(request):
    if request.method=='POST':
        form = DirectoryForm(request.POST, request.FILES)
        if form.save():
            return HttpResponse("Thanks")

    form = EventForm()
    return render(request, 'form_test.html', {'form': form})


def admin_form_test(request):
    form = NewsForm()

    if request.method=='POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("Thanks")

    return render(request, 'admin_form_test.html', {'form':form})

def profile_test(request):
    return render(request, 'profile.html')

def profile_edit_personal_test(request):
    return render(request, 'profile_form_personal.html')

def profile_edit_work_test(request):
    return render(request, 'profile_form_work.html')

def profile_edit_education_test(request):
    return render(request, 'profile_form_education.html')

def profile_link_test(request):
    return render(request, 'profile_link.html')