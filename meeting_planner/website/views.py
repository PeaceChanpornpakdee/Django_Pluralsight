from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html", {"message": "This data was sent from view to template", 'name':"Peace", 'age':20
    , "num_meetings": Meeting.objects.count()})

def about(request):
    return HttpResponse("My name is Peace")