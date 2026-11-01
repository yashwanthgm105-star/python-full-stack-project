
from django.contrib import admin
from django.urls import path
from jobs import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("job/<int:job_id>/", views.job_detail, name="job_detail"),
    path("job/<int:job_id>/apply/", views.apply_job, name="apply_job"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
