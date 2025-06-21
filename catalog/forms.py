from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Agent, Player, Transfer


class AgentCreationForm(UserCreationForm):
    class Meta:
        model = Agent
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirm Password"}
        )


class TransferCreationForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ["agent", "club", "transaction_amount", "player"]
        widgets = {
            "agent": forms.Select(attrs={"class": "form-select"}),
            "club": forms.Select(attrs={"class": "form-select"}),
            "transaction_amount": forms.NumberInput(attrs={"class": "form-control"}),
            "player": forms.Select(attrs={"class": "form-select"}),
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["first_name", "last_name", "age", "country", "position"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "position": forms.TextInput(attrs={"class": "form-control"}),
        }

positions = [
    ("GK", "Goalkeeper"),
    ("DF", "Defender"),
    ("MD", "Midfielder"),
    ("ST", "Striker"),
]

class PlayerSearchForm(forms.Form):
    last_name = forms.CharField(max_length=255, required=False)
    first_name = forms.CharField(max_length=255, required=False)
    country = forms.CharField(max_length=255, required=False)
    position = forms.ChoiceField(choices=positions, required=False)
    age = forms.IntegerField(required=False)
