__author__ = 'ankur'
from django.http import HttpResponse
from django.shortcuts import render
from AlumniPortal.forms import DirectoryForm, EventForm, NewsForm, AlumniUserForm, WorkDetailForm
from AlumniPortal.models import DegreeType, WORK_TYPE_CHOICES, WorkDetail, WorkType
from django.forms.models import modelformset_factory
from django import forms
from AlumniPortal.models import Event


def hello(request):
    return HttpResponse()


def form_test(request):
    if request.method == 'POST':
        form = DirectoryForm(request.POST, request.FILES)
        if form.save():
            return HttpResponse("Thanks")

    form = EventForm()
    return render(request, 'form_test.html', {'form': form})


def admin_form_test(request):
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("Thanks")

    return render(request, 'admin_form_test.html', {'form': form})


def profile_test(request):
    events = Event.objects.all()
    return render(request, 'profile.html', {'events': events})


def profile_edit_personal_test(request):
    marital_status_values = ['Single', 'Married']
    gender_values = ['Female', 'Male', 'Other']
    form = AlumniUserForm()
    return render(request, 'profile_form_personal.html', {'form': form,
                                                          'marital_status_values': marital_status_values,
                                                          'gender_values': gender_values})


def profile_edit_work_test(request):
    WorkDetailSet = modelformset_factory(WorkDetail, extra=10, max_num=10,
         # widgets={
         #     'degree_name': forms.TextInput(
         #         attrs={'html_type': "text", "html_tag": "input"}),
         #     'degree_type': forms.Select(
         #         attrs={'html_type': "text", "html_tag": "input"}),
         #     'field_of_study': forms.TextInput(
         #         attrs={'html_type': "text", "html_tag": "input"}),
         #     'start_date': forms.DateInput(
         #         attrs={'html_type': "date", "html_tag": "input"}),
         #     'end_date': forms.DateInput(
         #         attrs={'html_type': "date", "html_tag": "input"}),
         #     'school': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"})
         # }
         form=WorkDetailForm, fields=('title', 'work_type', 'start_date', 'end_date', 'organisation'))
    formset2 = WorkDetailSet(queryset=request.user.work_experience.all())
    visible_forms = 3
    work_type_values = WorkType.objects.order_by('id').values_list('name').distinct()

    work_type_values2 = []
    for ndx in range(len(work_type_values)):
        for choise in WORK_TYPE_CHOICES:
            if choise[0] == str(work_type_values[ndx][0]):
                work_type_values2 += [(choise[0], choise[1])]
    print str(formset2)
    return render(request, 'profile_form_work.html', {'formset': formset2, 'visible_forms': visible_forms,
                                                      'work_values': work_type_values2})

def work_details_html(request):
    return render(request, 'profile_form_work_form.html')

def profile_edit_education_test(request):
    return render(request, 'profile_form_education.html')


def profile_link_test(request):
    return render(request, 'profile_link.html')

def give_back(request):
    return render(request, 'give_back_backup_pycharm.html')

def prototype_filter(request):
    return render(request, 'prototype_filter.html')

def prototype_result(request):
    return render(request, 'prototype_result.html')

def testjson(request):
    return HttpResponse('{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1}, "objects": [{"educations": [{"degree_name": "knsfal", "end_date": "2015-03-04", "field_of_study": "ndlkn", "id": 1, "is_current": false, "resource_uri": "", "start_date": "2015-03-04"}], "email": "ankursial@gmail.com", "facebook_profile": "http://www.facebook.com/gupta.sauhard", "first_name": "ankur", "gender": null, "google_profile": "http://www.google.com/", "graduation_year": null, "homepage": "", "id": 1, "last_name": "sial", "linkedin_profile": "", "marital_status": "", "personal_email": null, "profile_photo": "http://media.giphy.com/media/zEO5eq3ZsEwbS/giphy.gif", "resource_uri": "/api/v1/current/1/", "twitter_profile": "", "work_details": [{"end_date": "2015-03-04", "is_current": false, "organisation": {"location": {"city": "test", "country": {"name": "abc", "resource_uri": "/api/v1/country/1/"}, "resource_uri": "/api/v1/location/1/"}, "name": "asdcsa", "resource_uri": "/api/v1/organisation/1/"}, "position": "tets", "resource_uri": "", "start_date": "2015-03-04", "title": "ank", "work_type": {"desc": "vsda", "name": "Non-Tech", "resource_uri": ""}}]}]}')