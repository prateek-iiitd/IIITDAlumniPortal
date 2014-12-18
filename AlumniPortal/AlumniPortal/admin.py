__author__ = 'Prateek'

from models import Award, NewsArticle, Degree, Student, Event, ContactPerson, ConvocationAward, Coordinator, \
    SpecialisationStream, Feedback
from models import AlumniUser, DegreeType, WorkType, WorkDetail, EducationDetail, Organisation, School

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth.models import Group


admin.site.register(Award)
admin.site.register(NewsArticle)
admin.site.register(Degree)
admin.site.register(Student)
admin.site.register(Event)
admin.site.register(ContactPerson)
admin.site.register(ConvocationAward)
admin.site.register(Coordinator)
admin.site.register(SpecialisationStream)
admin.site.register(Feedback)
admin.site.register(DegreeType)
admin.site.register(WorkType)
admin.site.register(WorkDetail)
admin.site.register(EducationDetail)
admin.site.register(Organisation)
admin.site.register(School)


class UserChangeForm(forms.ModelForm):
    # A form for updating users
    class Meta:
        model = AlumniUser
        fields = ['email', 'first_name', 'last_name', 'is_admin', 'gender', 'marital_status']


class UserCreationForm(forms.ModelForm):
    # A form for creating new users
    class Meta:
        model = AlumniUser
        fields = ('email', 'first_name', 'last_name')


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email',)
    list_filter = ('first_name',)
    fieldsets = (
        (None, {'fields': ('email', )}),
        ('Personal info',
         {'fields': ('first_name', 'last_name', 'gender', 'facebook_profile', 'linkedin_profile', 'google_profile',
                     'twitter_profile', 'homepage', 'marital_status', 'profile_photo', 'education', 'work_experience',
                     'graduation_year')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ()


admin.site.register(AlumniUser, MyUserAdmin)
admin.site.unregister(Group)