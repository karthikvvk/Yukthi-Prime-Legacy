# forms.py
from django import forms

class EventForm(forms.Form):
    eventName = forms.CharField(label='Event Name', max_length=100)
    venue = forms.CharField(label='Venue', max_length=100)
    dateTime = forms.DateTimeField(label='Date and Time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    duration = forms.CharField(label='Duration', max_length=100, required=False)
    guest = forms.CharField(label='Guest Speaker(s)', max_length=100, required=False)
    motto = forms.CharField(label='Motto/Moral/Subject/Agenda', max_length=100, required=False)
    targetAudience = forms.CharField(label='Target Audience', max_length=100, required=False)
    description = forms.CharField(label='Event Description', widget=forms.Textarea, required=False)
    organizer = forms.CharField(label='Organizer', max_length=100, required=False)
    registrationDetails = forms.CharField(label='Registration Details', widget=forms.Textarea, required=False)
    contactInfo = forms.CharField(label='Contact Information', max_length=100, required=False)
    eventImage = forms.ImageField(label='Event Image', required=False)
    sponsors = forms.CharField(label='Sponsors', max_length=100, required=False)
    dressCode = forms.CharField(label='Dress Code', max_length=100, required=False)
    behavioralExpectations = forms.CharField(label='General Instructions', widget=forms.Textarea, required=False)
