from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,('common/home.html'))

def about(request):
    return render(request,('common/about.html'))

def contact(request):
    return render(request,('common/contact.html'))

def shop(request):
    return render(request,('common/shop.html'))

def login(request):
    return render(request,('common/login.html'))

def signup(request):
    return render(request,('common/signup.html'))