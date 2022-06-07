from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html", {"message": "This data was sent from view to template", 'name':"Peace", 'age':20})

def about(request):
    return HttpResponse("My name is Peace")