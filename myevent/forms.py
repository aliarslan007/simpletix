from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'step': 60}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'ticket_price']
