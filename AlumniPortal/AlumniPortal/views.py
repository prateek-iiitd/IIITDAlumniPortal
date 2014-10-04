__author__ = 'Prateek'
from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from django.template.context import Context
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from forms import FeedbackForm
import json

from models import Student

def home(request):
    return render(request, 'home.html')

def directory(request):
    grad_years = Student.objects.values('graduation_year').distinct()
    return render(request, 'directory.html', {'grad_years': grad_years})

def contact_us(request):
    return render(request, 'contact_us.html')

def blog(request):
    return render(request, 'blog.html')

def news(request):
    return render(request, 'news.html')

def giveback(request):
    return render(request, 'giveback.html')

def get_by_batch(request):
    if request.is_ajax() and request.method=='GET':
        year = request.GET['year']
        students = Student.objects.filter(graduation_year=year)
        json_res = []
        for s in students:
            json_obj = dict(name = s.name,
                            iiitd_email = s.iiitd_email,
                            graduation_year = s.graduation_year,
                            degree = s.degree.name,
                            branch = s.degree.branch.name)
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
        print request.POST

        f = FeedbackForm(request.POST)
        f.save()

        return HttpResponse()

    else:
        return HttpResponseBadRequest()