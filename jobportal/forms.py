from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput
from django.core.validators import RegexValidator
from .models import Vacancy, ResumeUser
from datetime import date
from datetime import datetime
from .utils.getFilter_data import JsonParser


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
    REGIONS = JsonParser().tuple_regions("113")
    EXPERIENCE_CHOICES = (
        (True, "Есть опыт работы"),
        (False, "Нет опыта работы"),
    )

    region = forms.ChoiceField(choices=REGIONS, widget=forms.Select(attrs={'onClick': 'get_city()'}), label="Регион")
    city = forms.ChoiceField(choices=(), widget=forms.Select(attrs={"class": "hidden"}), label="Город")

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

    def clean_birthday(self):
        birthday = datetime.strptime(str(self.cleaned_data.get('birthday')), '%Y-%m-%d')
        today = date.today()

        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

        if age < 18:
            raise forms.ValidationError("Ваш возраст должен быть больше 18.")

        return self.cleaned_data.get('birthday')

    def clean_first_name(self):
        if not self.cleaned_data.get('first_name').isalpha():
            raise forms.ValidationError("Ваше имя содержит не корректные символы")
        
        return self.cleaned_data.get('first_name')
        
    def clean_last_name(self):
        if not self.cleaned_data.get('last_name').isalpha():
            raise forms.ValidationError("Ваша фамилия содержит не корректные символы")
        
        return self.cleaned_data.get('last_name')

    def clean_title(self):

        lenght = len(self.cleaned_data.get('title'))
        if lenght < 5 or lenght > 50:
            raise forms.ValidationError("Слишком короткий заголовок. Используйте от 5 до 50 символов.")
        
        return self.cleaned_data.get('title')

    class Meta:
        model = ResumeUser

        phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
        fields = ["title", "first_name", "last_name", "phone_number", "region", "city", "birthday", "gender", "citizenship", "excpirience_sum", "salary"]
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
            "region": "Регион",
            "city": "Город",
            "birthday": "Дата рождения",
            "gender": "Пол",
            "citizenship": "Гражданство",
            "excpirience_sum": "Опыт работы",
            "salary": "Зарплата"
        }
