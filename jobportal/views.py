from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import UserLoginForm
from .forms import UserRegistrationForm
from .forms import VacancyForm
from .models import UserProfile
from .models import Vacancy


@login_required
def create_vacancy(request):
    if request.user.profile.role != "Рекрутер":
        return redirect("vacancy_board")

    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.created_by = request.user
            vacancy.save()
            return redirect("vacancy_board")
    else:
        form = VacancyForm()

    return render(request, "create_vacancy.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile.objects.create(user=user, role="Кандидат")
            login(request, user)
            return redirect("login")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def vacancy_board(request):
    vacancies = Vacancy.objects.filter(status=True)
    return render(request, "vacancy_board.html", {"vacancies": vacancies})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("vacancy_board")
    else:
        form = UserLoginForm()

    return render(request, "login.html", {"form": form})
