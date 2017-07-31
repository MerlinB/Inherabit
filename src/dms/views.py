from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DMSForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Switch


@login_required(login_url = reverse_lazy('framework:login'))
def dashboard_view(request):
    if request.method == 'POST':
        newswitch = Switch(controller=request.user.controller, timeframe=request.POST['timeframe'])
        newswitch.save()
    login_message = "You are logged in as %s!" % request.user.username
    form = DMSForm(user = request.user)
    
    context = {
        'form': form,
        'switches': list(Switch.objects.filter(controller__user=request.user)),
        'login_message': login_message
    }
    return render(request, 'dms/dashboard-view.html', context)
