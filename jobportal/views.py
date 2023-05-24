from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserLoginForm
from .forms import UserRegistrationForm
from .forms import VacancyForm, ResumeForm
from .models import UserProfile
from .models import Resume, ResumeUser
from .utils.parse_hh_data import parseHh, FilterUrl
from django.core.paginator import Paginator
from .utils.getFilter_data import FilterData

@login_required
def create_vacancy(request):
    if request.user.profile.role != "Рекрутер":
        return redirect("resume_board")

    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.created_by = request.user
            vacancy.save()
            return redirect("resume_board")
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


def resume_board(request):
    hh_filter = FilterUrl().create_url(
        request.GET.get("only_gender", False),
        request.GET.get("gender", "unknown"),
        request.GET.getlist("area", [113]),
        request.GET.get("work_exp1t3", False),
        request.GET.get("work_exp3t6", False),
        request.GET.get("work_exp_noExperience", False),
        request.GET.get("work_exp_more", False)
    )
    hh = parseHh(hh_filter)
    page = request.GET.get("page", 0)
    serp = hh.get_serp(page)
    resumes = []
    for j in range(len(serp)):
        resume = hh.parse_single_resume(serp[j])
        resumes.append(
            {
                "id": resume["id"],
                "title": resume["title"],
                "age": resume["age"],
                "resume_status": resume["resume_status"],
                "excpirience_sum": resume["excpirience_sum"],
                "last_experience_link": resume["last_experience_link"],
                "last_update": resume["last_update"],
                "title_url": resume["title_url"],
                "salary": resume["salary"]
            }
        )

    filters = FilterData().get_area()

    return render(request, "resume_board.html", 
                {
                    "resumes": resumes, 
                    "page": page, 
                    "count_pages": 250,
                    "url": "&%s" %hh_filter[1:],
                    "areas": {
                        "current": {
                            "name": filters["name"],
                            "id": filters["id"]
                        },
                        "all": filters["areas"]
                    },
                    "current_url": "resumes"
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
                return redirect("resume_board")
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

def create_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit = False)
            resume.created_by = request.user
            resume.save()
            return redirect("resume_board")
    else:
        form = ResumeForm()
    return render(request, "create_resume.html", {"form": form})