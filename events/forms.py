from django import forms
from events.models import Event
from django.utils.timezone import now

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['slogan', 'location', 'start_time', 'available_tickets', 'key_features', 'banner_url']
        widgets = {
            'slogan': forms.TextInput(attrs={'placeholder': 'Provide an appealing text...'}),
            'location': forms.TextInput(),
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'available_tickets': forms.NumberInput(attrs={'placeholder': 'Enter number of tickets', 'min': '0', 'value': ''}),
            'key_features': forms.Textarea(attrs={'placeholder': 'Provide important event details...'}),
            'banner_url': forms.URLInput(attrs={'placeholder': 'An optional banner image URL...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default start_time to now
        if not self.initial.get('start_time'):
            self.initial['start_time'] = now().strftime('%Y-%m-%dT%H:%M')