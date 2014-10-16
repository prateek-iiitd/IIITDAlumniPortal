from django.db.models.fields import CharField

__author__ = 'Prateek'

from django import forms
from models import Feedback, NewsArticle, Event
import csv
#from django.forms import widgets

from models import Degree

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['headline', 'article', 'occurred_on', 'large_img', 'reporter', 'gallery_link']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['starts_at'].widget = widgets.AdminSplitDateTime()

DegreeChoices = (('B.Tech.', 'B.Tech.'), ('M.Tech.', 'M.Tech.'), ('Ph.D.', 'Ph.D.'), ('Dual', 'Dual'))


class DirectoryForm(forms.Form):
    degree = forms.ChoiceField(choices=DegreeChoices)
    passing_year = forms.IntegerField()
    file = forms.FileField(label='Select a CSV file to import:',)

    def save(self):
        csv_file = self.cleaned_data['file']
        records = csv.reader(csv_file, dialect=csv.excel_tab)
        for row in records:
            print row