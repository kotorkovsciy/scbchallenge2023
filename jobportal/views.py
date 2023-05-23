from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserLoginForm
from .forms import UserRegistrationForm
from .forms import VacancyForm
from .models import UserProfile
from .models import Resume
from .utils.parse_hh_data import parseHh, FilterUrl
from django.core.paginator import Paginator

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


def vacancy_board(request, page=0):
    vacancies = Resume.objects.filter()
    count_pages = round(vacancies.count() / 10)
    start_page = page*10
    end_page = start_page + 10
    return render(request, "vacancy_board.html", 
                {
                    "vacancies": vacancies[start_page:end_page], 
                    "page": page, 
                    "count_pages": count_pages
                }
    )

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

def update_resumes(request):
    if request.method != "POST":
        hh_filter = FilterUrl().create_url()
        hh = parseHh(hh_filter)
        for i in range(20):
            serp = hh.get_serp(i)
            for j in range(len(serp)):
                resume = hh.parse_single_resume(serp[j])
                if not Resume.objects.filter(id=resume["id"]).exists():
                    Resume.objects.create(
                        id=resume["id"],
                        title=resume["title"],
                        age=resume["age"],
                        resume_status=resume["resume_status"],
                        excpirience_sum=resume["excpirience_sum"],
                        last_experience_link=resume["last_experience_link"],
                        last_update=resume["last_update"],
                        title_url=resume["title_url"],
                        salary=resume["salary"]
                    )
                else:
                    pass
                    # TODO: если resume не активно, то удалить

        return HttpResponse()
    
    return HttpResponse(status=404)
