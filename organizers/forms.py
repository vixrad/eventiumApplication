from django import forms
from organizers.models import Organizer


class OrganizerCreateForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['company_name', 'phone_number', 'secret_key', 'website']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Enter a company name...'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter a valid phone number (digits only)...'
            }),
            'secret_key': forms.PasswordInput(attrs={
                'placeholder': 'Enter a secret key like <1234>...'
            }),
            'website': forms.URLInput(attrs={
                'placeholder': 'Enter your website (optional)...'
            }),
        }

class OrganizerEditForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['company_name', 'phone_number', 'website']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Enter a company name...'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter a valid phone number (digits only)...'
            }),
            'website': forms.URLInput(attrs={
                'placeholder': 'Enter your website (optional)...'
            }),
        }