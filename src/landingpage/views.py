from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'landingpage/home-view.html', {})

def start_view(request):
    return HttpResponse('This site is under construction.')

def faq_view(request):
    return render(request, 'landingpage/faq-view.html')

def about_view(request):
    return render(request, 'landingpage/about-view.html')
