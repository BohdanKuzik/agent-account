# catalog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Agent


class AgentCreationForm(UserCreationForm):
    class Meta:
        model = Agent
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
