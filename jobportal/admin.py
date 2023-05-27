from django.contrib import admin

from .models import Candidate
from .models import Message
from .models import RecruitmentStage
from .models import Statistic
from .models import UserProfile
from .models import Vacancy
from .models import ResumeUser

admin.site.register(UserProfile)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["title", "created_by", "deadline", "status"]
    list_filter = ["status", "created_by"]
    search_fields = ["title"]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "contact_info", "status"]
    list_filter = ["status", "recruiter"]
    search_fields = ["first_name", "last_name", "contact_info"]


@admin.register(RecruitmentStage)
class RecruitmentStageAdmin(admin.ModelAdmin):
    list_display = ["name", "start_date", "end_date", "status", "candidate"]
    list_filter = ["status"]
    search_fields = ["name"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["sender", "recipient", "timestamp"]
    list_filter = ["sender", "recipient"]
    search_fields = ["content"]


admin.site.register(Statistic)

admin.site.register(ResumeUser)
