from django import forms

from .models import Contact_Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Message
        fields = ['name', 'email', 'phone', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Name',
            'class': 'flex-1 outline-none bg-transparent'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'class': 'w-full outline-none bg-transparent'
        })
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Phone',
            'class': 'flex-1 outline-none bg-transparent'
        })
        self.fields['message'].widget.attrs.update({
            'placeholder': 'Enter your message here...',
            'class': 'w-full rounded-xl h-64 max-h-64 min-h-64 bg-gray-200 outline-none px-8 py-4'
        })
