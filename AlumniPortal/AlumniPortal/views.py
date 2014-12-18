__author__ = 'Prateek'
from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from django.template.context import Context
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from forms import FeedbackForm, NewsForm, EventForm, DirectoryForm
import json
from models import NewsArticle, Event

from models import Student, Degree


def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events, })


def directory(request):
    grad_years = Student.objects.values('graduation_year').distinct()
    return render(request, 'directory.html', {'grad_years': grad_years})


def contact_us(request):
    return render(request, 'contact_us.html')


def blog(request):
    events = Event.objects.all()
    return render(request, 'blog.html', {'events': events, })


def news(request):
    news_articles = NewsArticle.objects.all()
    events = Event.objects.all()
    return render(request, 'news.html',
                  {
                      'news_articles': news_articles,
                      'events': events,
                  })


def giveback(request):
    return render(request, 'giveback.html')


def admin_forms(request):
    degree_values = Degree.objects.values('name').distinct()
    news_form = NewsForm()
    event_form = EventForm()
    directory_form = DirectoryForm()
    return render(request, 'admin_forms.html',
                  {'degree_values': degree_values, 'news_form': news_form, 'event_form': event_form,
                   'directory_form': directory_form, 'news_class': "active"})


def get_by_batch(request):
    if request.is_ajax() and request.method == 'GET':
        year = request.GET['year']
        students = Student.objects.filter(graduation_year=year).order_by('name')
        json_res = []
        for s in students:
            json_obj = dict(name=s.name,
                            iiitd_email=s.iiitd_email,
                            graduation_year=s.graduation_year,
                            degree=s.degree.name,
                            branch=s.degree.branch.name)
            if s.degree.specialisation:
                json_obj['specialisation'] = s.degree.specialisation.name
            json_res.append(json_obj)

        c = Context()
        template = get_template('card_contact2.html').render(RequestContext(request))
        resp = {'students': json_res, 'html': template}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def feedback(request):
    if request.method == 'POST' and request.is_ajax():
        f = FeedbackForm(request.POST)
        f.save()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def add_news(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES)
        if news_form.is_valid():
            news_form.save()
            return HttpResponseRedirect('/admin_forms/')
        else:
            degree_values = Degree.objects.values('name').distinct()
            event_form = EventForm()
            directory_form = DirectoryForm()
            return render(request, 'admin_forms.html',
                          {'degree_values': degree_values, 'news_form': news_form, 'event_form': event_form,
                           'directory_form': directory_form, 'news_class': "active"})
    else:
        return HttpResponseBadRequest("THE REQUESTED URL IS INVALID")


def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return HttpResponseRedirect('/admin_forms/')
        else:
            degree_values = Degree.objects.values('name').distinct()
            news_form = NewsForm()
            directory_form = DirectoryForm()
            return render(request, 'admin_forms.html',
                          {'degree_values': degree_values, 'news_form': news_form, 'event_form': event_form,
                           'directory_form': directory_form, 'event_class': "active"})

    else:
        return HttpResponseBadRequest("THE REQUESTED URL IS INVALID")


def add_directory(request):
    if request.method == 'POST':
        directory_form = DirectoryForm(request.POST, request.FILES)
        if directory_form.is_valid():
            directory_form.save()
            return HttpResponseRedirect('/admin_forms/')
        else:
            degree_values = Degree.objects.values('name').distinct()
            news_form = NewsForm()
            event_form = EventForm()
            return render(request, 'admin_forms.html',
                          {'degree_values': degree_values, 'news_form': news_form, 'event_form': event_form,
                           'directory_form': directory_form, 'directory_class': "active"})
    else:
        return HttpResponseBadRequest("THE REQUESTED URL IS INVALID")


def add_blog(request):
    if request.method == 'POST':
        return HttpResponse("Accepted")

    return HttpResponseBadRequest