# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
import random

def my_form_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form 
            img = f"{random.randrange(1,3)}.jpg"
            d = {
            'eventName' : form.cleaned_data['eventName'],
            'venue' : form.cleaned_data['venue'],
            'dateTime' : form.cleaned_data['dateTime'],
            'duration' : form.cleaned_data['duration'],
            'guest' : form.cleaned_data['guest'],
            'motto' : form.cleaned_data['motto'],
            'targetAudience' : form.cleaned_data['targetAudience'],
            'description' : form.cleaned_data['description'],
            'organizer' : form.cleaned_data['organizer'],
            'registrationDetails' : form.cleaned_data['registrationDetails'],
            'contactInfo' : form.cleaned_data['contactInfo'],
            'eventImage' : form.cleaned_data['eventImage'],
            'sponsors' : form.cleaned_data['sponsors'],
            'dressCode' : form.cleaned_data['dressCode'],
            'behavioralExpectations' : form.cleaned_data['behavioralExpectations']}
            print(d, img)
            # For example, return a success message
            return render(request, "res.html", {"events":d, 'img':img})

    else:
        form = EventForm()
    return render(request, 'index.html', {'form': form})

def home(request):
    return render(request, 'main.html')