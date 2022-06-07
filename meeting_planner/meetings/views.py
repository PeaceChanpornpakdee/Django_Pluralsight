from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from meetings.models import Meeting, Room

# Create your views here.

def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def room(request):
    return render(request, "meetings/room.html", {"rooms": Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})