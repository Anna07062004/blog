from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def post_detail(request):
    return render(request, "post_detail.html")

def user_login(request):
    return render(request, "users/login.html")

def user_registr(request):
    return render(request, "users/registr.html")