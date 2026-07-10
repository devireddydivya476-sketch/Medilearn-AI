from django.urls import path
from . import views


urlpatterns = [

    # Home
    path("", views.home, name="home"),


    # Authentication
    path("login/", views.login_view, name="login"),

    path("signup/", views.signup_view, name="signup"),

    path("logout/", views.user_logout, name="logout"),


    # User Pages
    path("profile/", views.profile, name="profile"),

    path("dashboard/", views.dashboard, name="dashboard"),


    # MediLearn AI Story Pages

    path("read/", views.read_story, name="read"),

    path("audio/", views.audio_page, name="audio"),

    path("video/", views.video_page, name="video"),

    path("animation/", views.animation_page, name="animation"),

]