from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput
from django.core.validators import RegexValidator
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
    EXPERIENCE_CHOICES = (
        (True, "Есть опыт работы"),
        (False, "Нет опыта работы"),
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'. Допустимая длина составляет от 9 до 15 цифр."
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel'}),
        validators=[phone_regex],
        label="Номер телефона"
    )
    excpirience_sum = forms.ChoiceField(choices=EXPERIENCE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'experience-field'}), label="Опыт работы")

    class Meta:
        model = ResumeUser
        phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
        fields = ["title", "first_name", "last_name", "phone_number", "city", "birthday", "gender", "citizenship", "excpirience_sum", "salary"]
        widgets = {
            "birthday": DateInput(attrs={"type": "date"}), 
            "phone_number": DateInput(attrs={"type": "tel"}),
            "title": forms.TextInput(attrs={"type": "text"}),
            "first_name": forms.TextInput(attrs={"type": "text"}),
            "last_name": forms.TextInput(attrs={"type": "text"}),
        }
        labels = {
            "title": "Заголовок",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "phone_number": "Номер телефона",
            "city": "Город",
            "birthday": "Дата рождения",
            "gender": "Пол",
            "citizenship": "Гражданство",
            "excpirience_sum": "Опыт работы",
            "salary": "Зарплата"
        }
