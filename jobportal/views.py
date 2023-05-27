from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .forms import UserLoginForm
from .forms import UserRegistrationForm
from .forms import VacancyForm, ResumeForm
from .models import UserProfile
from .models import Resume, ResumeUser
from .utils.parse_hh_data import parseHh, FilterUrl
from django.core.paginator import Paginator
from .utils.getFilter_data import FilterData, JsonParser
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

def unauthenticated_user(view_func):
    @user_passes_test(lambda user: not user.is_authenticated, login_url='resume_board')
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper_func

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

@unauthenticated_user
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
    page = request.GET.get("page", 0)

    filters = {}

    if request.GET.get("gender", "unknown") != "unknown":
        filters["gender"] = request.GET.get("gender")

    resumes = ResumeUser.objects.filter(
        **filters
    )

    start = int(page) * 19
    end = start + 19

    resumes = list(resumes[start:end])

    if len(resumes) < 19:
        amount = 19 - len(resumes)
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
        for j in range(amount):
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
                    "salary": resume["salary"],
                    "from_resume": "hh",
                }
            )

    reg = JsonParser().get_republics_by_country_n_republics_ids("113", request.GET.getlist("area", ["113"]))
    specializations = FilterData().get_specializations()

    return render(request, "resume_board.html", 
                {
                    "resumes": resumes, 
                    "page": page, 
                    "count_pages": 250,
                    "url": "&%s" %hh_filter[1:],
                    "areas": reg,
                    "current_url": "resumes",
                    "gender": request.GET.get("gender", "unknown"),
                    "specializations": specializations
                }
    )

@unauthenticated_user
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

@login_required
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
    return render(request, "create_resume.html", {"form": form, "current_url": "create-resume"})

@login_required
def resume_detail(request, id):
    resume = ResumeUser.objects.get(id=id)
    return render(request, "resume_detail.html", {"resume": resume, "current_url": "create-resume"})

@login_required
def profile_detail(request, id):
    profile = User.objects.get(id=id)
    resume = ResumeUser.objects.filter(created_by=id)
    return render(request, "profile_detail.html", {"profile": profile, "resumes": resume, "current_url": "create-resume"})

@login_required
def resume_delete(request):
    data = json.loads(request.body)
    if request.headers["X-CSRFToken"] == request.COOKIES["csrftoken"]:
        resume = ResumeUser.objects.get(id=data.get("id"))
        if resume.created_by.id == request.user.id:
            resume.delete()
            return JsonResponse(
                    {
                        "message": "Резюме успешно удалено"
                    },
                    status = 200
                )
        else:
            return JsonResponse(
                    {
                        "message": "Вы не можете удалить чужое резюме"
                    },
                    status = 400
                )
    else:
        return JsonResponse(
                {
                    "message": "CSRF verification failed."
                },
                status = 400
            )
