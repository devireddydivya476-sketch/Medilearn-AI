from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Home Page
def home(request):
    return render(request, "home.html")


# Login
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


# Signup
def signup_view(request):

    if request.method == "POST":

        fullname = request.POST["fullname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]


        if password != confirm_password:

            return render(request, "signup.html", {
                "error": "Passwords do not match"
            })


        user = User.objects.create_user(
            username=fullname,
            email=email,
            password=password
        )

        user.save()

        return redirect("login")


    return render(request, "signup.html")



# Profile
@login_required
def profile(request):
    return render(request, "profile.html")



# Logout
def user_logout(request):

    logout(request)

    return redirect("login")



# Dashboard
@login_required
def dashboard(request):

    return render(request, "dashboard.html")



# ============================
# MediLearn AI Story Module
# ============================


def read_story(request):

    return render(request, "read.html")



def audio_page(request):

    return render(request, "audio.html")



def video_page(request):

    return render(request, "video.html")



def animation_page(request):

    return render(request, "animation.html")