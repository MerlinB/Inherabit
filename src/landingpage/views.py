from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/admin/login')
def home_view(request):
    return render(request, 'landingpage/home-view.html', {})

def start_view(request):
    return HttpResponse('This site is under construction.')
