from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput

from .models import Vacancy, ResumeUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ["title", "description", "requirements", "deadline", "status"]
        widgets = {"deadline": DateInput(attrs={"type": "date"})}

class ResumeForm(forms.ModelForm):

    class Meta:
        model = ResumeUser
        phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
        fields = ["first_name", "last_name", "phone_number", "city", "birthday", "gender", "citizenship", "excpirience_sum", "title", "salary"]
        widgets = {"birthday": DateInput(attrs={"type": "date"}), "phone_number": DateInput(attrs={"type": "tel"})}
