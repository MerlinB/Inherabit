from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Logged in")
            return redirect(reverse('dms:dashboard'))
        else:
            # return HttpResponse("Wrong User/PW.")
            messages.info(request, 'Wrong User/Password.')

    if request.user.is_authenticated():
        return redirect(reverse('dms:dashboard'))
    form = LoginForm
    
    context = {
        'form': form, 
        'header': 'Log In', 
        'button': ['Sign Up',reverse('framework:signup')]
    }
    
    return render(request, 'framework/signup-view.html', context)
    
        
def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect(reverse('framework:login'))
    

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print("User created")
            return redirect(reverse('dms:dashboard'))
        else:
            return HttpResponse("Errors:",form.errors)
    else:
        if request.user.is_authenticated():
            return redirect(reverse('dms:dashboard'))
        form = SignUpForm()
        
        context = {
            'form': form, 
            'header': 'Sign Up',
            'button': ['Log In',reverse('framework:login')]
        }
    
        return render(request, 'framework/signup-view.html', context)
