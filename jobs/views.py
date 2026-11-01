
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Job, JobApplication


def home(request):
    jobs = Job.objects.all().order_by("-created_at")
    return render(request, "jobs/home.html", {"jobs": jobs})


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "jobs/job_detail.html", {"job": job})


def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        applicant_name = request.POST.get("applicant_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        cover_letter = request.POST.get("cover_letter", "").strip()
        resume = request.FILES.get("resume")

        if applicant_name and email and phone:
            JobApplication.objects.create(
                job=job,
                applicant_name=applicant_name,
                email=email,
                phone=phone,
                cover_letter=cover_letter,
                resume=resume,
            )

            return render(
                request,
                "jobs/application_success.html",
                {"job": job},
            )

        messages.error(request, "Please fill in all required fields.")

    return render(request, "jobs/apply.html", {"job": job})


def register(request):
  

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "jobs/register.html", {"form": form})

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def user_login(request):
   

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "jobs/login.html", {"form": form})


def user_logout(request):
    if request.method == "POST":
        logout(request)

    return redirect("home")

