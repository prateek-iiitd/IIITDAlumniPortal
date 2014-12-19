__author__ = 'Prateek'

from django import forms
from models import Feedback, NewsArticle, Event, Branch, SpecialisationStream, Student, AlumniUser, EducationDetail, WorkDetail
import csv

from models import Degree


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['headline', 'article', 'occurred_on', 'large_img', 'gallery_link', 'reporter']
        widgets = {
            'headline': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'article': forms.Textarea(attrs={'html_tag': 'textarea'}),
            'occurred_on': forms.TextInput(attrs={'html_type': "date", "html_tag": "input"}),
            'large_img': forms.ClearableFileInput(attrs={'html_type': "file", "html_tag": "input"}),
            'reporter': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'gallery_link': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        widgets = {
            'title': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'description': forms.Textarea(attrs={'html_tag': 'textarea'}),
            'venue': forms.TextInput({'html_type': "text", "html_tag": "input"}),
            'starts_at': forms.TextInput({'html_type': "datetime", "html_tag": "input"}),
            'external_link': forms.TextInput({'html_type': "text", "html_tag": "input"}),
        }


DegreeChoices = (('B.Tech.', 'B.Tech.'), ('M.Tech.', 'M.Tech.'), ('Ph.D.', 'Ph.D.'), ('Dual', 'Dual'))


class DirectoryForm(forms.Form):
    degree = forms.ChoiceField(choices=DegreeChoices)
    degree.widget = forms.Select(attrs={'html_type': "text", "html_tag": "input"})
    passing_year = forms.IntegerField(min_value=2012)
    passing_year.widget = forms.TextInput(attrs={'html_type': "file", "html_tag": "input"})
    csv_file = forms.FileField(label='CSV File', )
    csv_file.widget = forms.ClearableFileInput({'html_type': "file", "html_tag": "input"})


    def save(self):
        if self.is_valid():
            csv_file = self.cleaned_data['csv_file']
            records = csv.reader(csv_file, dialect=csv.excel_tab, delimiter=',')
            # skip header
            next(records, None)
            year, degree = str(self.cleaned_data['passing_year']), str(self.cleaned_data['degree'])

            for row in records:
                name, email, branch, specialization = row
                branch = Branch.objects.get(name=branch)

                if specialization == '':
                    stream = None
                else:
                    if not SpecialisationStream.objects.filter(name=specialization).exists():
                        stream = SpecialisationStream(name=specialization)
                        stream.save()
                    stream = SpecialisationStream.objects.get(name=specialization)

                if not Degree.objects.filter(name=degree, branch=branch, specialisation=stream):
                    new_degree = Degree(name=degree, branch=branch, specialisation=stream)
                    new_degree.save()
                student_degree = Degree.objects.get(name=degree, branch=branch, specialisation=stream)

                student = Student(name=name, iiitd_email=email, graduation_year=int(year), degree=student_degree)
                student.save()
        else:
            print self.errors


class AlumniUserForm(forms.ModelForm):
    class Meta:
        model = AlumniUser
        fields = ['email', 'personal_email', 'gender', 'marital_status', 'profile_photo',
                  'linkedin_profile', 'facebook_profile', 'google_profile', 'twitter_profile', 'homepage']
        widgets = {
            'first_name': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'last_name': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'email': forms.EmailInput(attrs={'html_type': "text", "html_tag": "input"}),
            'personal_email': forms.EmailInput(attrs={'html_type': "text", "html_tag": "input"}),
            'gender': forms.Select(attrs={'html_type': "text", "html_tag": "input"}),
            'marital_status': forms.Select(attrs={'html_type': "text", "html_tag": "input"}),
            'profile_photo': forms.ClearableFileInput({'html_type': "file", "html_tag": "input"}),
            'linkedin_profile': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'facebook_profile': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'google_profile': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'twitter_profile': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'homepage': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"})
        }


class EducationDetailForm(forms.ModelForm):
    class Meta:
        model = EducationDetail
        # fields = ['education']
        widgets = {
            'degree_name' : forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'degree_type':  forms.Select(attrs={'html_type': "text", "html_tag": "input"}),
            'field_of_study': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'start_date': forms.DateInput(attrs={'html_type': "date", "html_tag": "input"}),
            'end_date': forms.DateInput(attrs={'html_type': "date", "html_tag": "input"}),
            'school': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"})
        }


class WorkDetailForm(forms.ModelForm):
    class Meta:
        model = WorkDetail
        fields = ['title', 'work_type', 'start_date', 'end_date', 'organisation']
        widgets = {
            'title' : forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'work_type':  forms.Select(attrs={'html_type': "text", "html_tag": "input"}),
            'start_date': forms.DateInput(attrs={'html_type': "date", "html_tag": "input"}),
            'end_date': forms.DateInput(attrs={'html_type': "date", "html_tag": "input"}),
            'organisation': forms.TextInput(attrs={'html_type': "text", "html_tag": "input"}),
            'id': forms.TextInput(attrs={'html_type': "hidden", "html_tag": "input"})
        }