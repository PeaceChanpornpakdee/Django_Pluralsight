from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html")

def about(request):
    return HttpResponse("My name is Peace")