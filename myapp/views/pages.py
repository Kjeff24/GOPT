from django.shortcuts import render, redirect

def home(request):
    return render(request, "user_pages/homepage.html")

def about(request):
    return render(request, "user_pages/about.html")