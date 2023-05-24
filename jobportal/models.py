from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import date
from datetime import datetime
from django.db.models.functions import ExtractYear

class UserProfile(models.Model):
    ROLES = (
        ("HRBP", "HRBP"),
        ("Заказчик", "Заказчик"),
        ("Рекрутер", "Рекрутер"),
        ("Кандидат", "Кандидат"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLES)


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    deadline = models.DateField()
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_vacancies"
    )


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=100)
    resume = models.FileField(upload_to="resumes/")
    status = models.CharField(max_length=20)
    applied_to = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name="applicants"
    )
    recruiter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recruited_candidates"
    )


class RecruitmentStage(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="stages"
    )


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Statistic(models.Model):
    vacancies_count = models.IntegerField()
    candidates_count = models.IntegerField()
    stages_count = models.IntegerField()

class Resume(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    title_url = models.TextField()
    salary = models.TextField()
    age = models.TextField()
    resume_status = models.TextField()
    excpirience_sum = models.TextField()
    last_experience_link = models.TextField()
    last_update = models.TextField()

class ResumeUser(models.Model):
    GENDERS = (
        ("Мужской", "Мужской"),
        ("Женский", "Женский"),
    )
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.TextField()
    city = models.TextField()
    birthday = models.DateField()
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=10)
    citizenship = models.TextField()
    excpirience_sum = models.BooleanField()
    title = models.TextField()
    salary = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_resume"
    )
    def save(self, *args, **kwargs):
        self.age = int(date.today().strftime("%Y")) - int(self.birthday.strftime("%Y"))
        super(ResumeUser, self).save(*args, **kwargs)