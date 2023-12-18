from rest_framework import serializers

from .models import Vacancy, Responses, ResumeUser


class ResumeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUser
        fields = (
             "__all__"
        )

class VacancySummarySerializer(serializers.ModelSerializer):
    amount_responses = serializers.IntegerField()
    class Meta:
        model = Vacancy
        fields = (
            "title",
            "amount_responses",
        )

class ResponsesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="resume.title", read_only=True)
    class Meta:
        model = Responses
        fields = (
            "id",
            "title",
            "created_at"
            )
        
class ResponseSerializer(serializers.ModelSerializer):
    resume = ResumeUserSerializer(read_only=True)
    class Meta:
        model = Responses
        fields = (
            "__all__"
            )
