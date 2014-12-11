__author__ = 'Prateek'

from django import forms
from models import Feedback, NewsArticle, Event
import csv
# from django.forms import widgets

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
    degree.widget = forms.TextInput(attrs={'html_type': "text", "html_tag": "input"})
    passing_year = forms.IntegerField()
    passing_year.widget = forms.TextInput(attrs={'html_type': "file", "html_tag": "input"})
    csv_file = forms.FileField(label='CSV File', )
    csv_file.widget = forms.ClearableFileInput({'html_type': "file", "html_tag": "input"})


    def save(self):
        if self.is_valid():
            csv_file = self.cleaned_data['csv_file']
            records = csv.reader(csv_file, dialect=csv.excel_tab)
            for row in records:
                print row
        else:
            print self.errors