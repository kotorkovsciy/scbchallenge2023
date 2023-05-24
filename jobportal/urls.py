from django.contrib.auth import views as auth_views
from django.urls import path

from .views import create_vacancy
from .views import login_view
from .views import register_view
from .views import resume_board
from .views import update_resumes

urlpatterns = [
    path("user/register/", register_view, name="user_registration"),
    path("resumes/", resume_board, name="resume_board"),
    path("login/", login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("create-vacancy/", create_vacancy, name="create_vacancy"),
    path("update_resumes/", update_resumes)
]
