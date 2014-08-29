__author__ = 'Prateek'

from django.contrib import admin
from models import Award, NewsArticle, Degree, Student, Event, ContactPerson, ConvocationAward, Coordinator, SpecialisationStream

admin.site.register(Award)
admin.site.register(NewsArticle)
admin.site.register(Degree)
admin.site.register(Student)
admin.site.register(Event)
admin.site.register(ContactPerson)
admin.site.register(ConvocationAward)
admin.site.register(Coordinator)
admin.site.register(SpecialisationStream)