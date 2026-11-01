
from django.contrib import admin
from .models import Job, JobApplication


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "salary")


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "applicant_name",
        "job",
        "email",
        "phone",
        "applied_at",
    )
    list_filter = ("job", "applied_at")
    search_fields = ("applicant_name", "email")
