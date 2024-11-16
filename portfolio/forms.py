from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
    
    # Custom validation for message length
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 15:
            raise forms.ValidationError("Your message must be at least 15 characters.")
        return message
