from django.contrib.auth import views as auth_views

from django.urls import path, include

from .views import create_vacancy, create_resume
from .views import login_view, logout_view
from .views import register_view
from .views import resume_board
from .views import update_resumes, resume_detail, profile_detail
from .views import resume_delete, get_cities, get_area
from .views import vacancy_board, vacancy_detail
from .views import get_resumes_user, AmountResponses, VacancyResponse, VacancyResponses

urlpatterns = [
    path("user/register/", register_view, name="user_registration"),
    path("resumes/", resume_board, name="resume_board"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create-vacancy/", create_vacancy, name="create_vacancy"),
    path("update_resumes/", update_resumes),
    path("create-resume/", create_resume, name="create_resume"),
    path("resumes/resume/<int:id>/", resume_detail, name="resume_detail"),
    path("profile/<int:id>/", profile_detail, name="profile"),
    path("vacancies/", vacancy_board, name="vacancy_board"),
    path("vacancies/vacancy/<int:id>/", vacancy_detail, name="vacancy_detail"),
    path("resume_delete/", resume_delete),
    path("get_cities/", get_cities),
    path("get_area/", get_area),
    path("get_resumes_user/", get_resumes_user),
    path("api/get_amount_responses/", AmountResponses.as_view()),
    path("api/get_response/", VacancyResponse.as_view()),
    path("api/get_responses/", VacancyResponses.as_view()),
    path("api/auth/", include("djoser.urls.authtoken")),
]
