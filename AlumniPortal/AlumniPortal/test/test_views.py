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


def profile_edit_education_test(request):
    return render(request, 'profile_form_education.html')


def profile_link_test(request):
    return render(request, 'profile_link.html')

def give_back(request):
    return render(request, 'give_back.html')