from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Authentication pages
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.user_logout, name="logout"),

    # User pages
    path("profile/", views.profile, name="profile"),
]
path("dashboard/", views.dashboard, name="dashboard"),