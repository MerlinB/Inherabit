from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DMSForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Switch
#import os
from django.core.mail import send_mail
from .utils import resetTimer

@login_required(login_url = reverse_lazy('framework:login'))
def dashboard_view(request):
    if request.method == 'POST':
        form = DMSForm(request.POST)
        if request.POST['notification'] > request.POST['timeframe']:
            messages.error(request, "Notification can't be bigger than the timeframe.")
        elif form.is_valid():
            newswitch = form.save(commit=False)
            newswitch.controller = request.user.controller
            newswitch.save()
            # Old solution:
            # newswitch = Switch(controller=request.user.controller, *args, **kwargs)#, timeframe=request.POST['timeframe'], notification=request.POST['notification'])
            # newswitch.save()
            messages.info(request, 'DMS created.')
        # send_mail(
        #     'DMS created',
        #     'Test',
        #     'info@inherabit.com',
        #     [request.user.email],
        #     fail_silently=False,
        # )
        #os.system('(crontab -l ; echo "0 4 * * * myscript")| crontab')
    resetTimer(request.user)

    login_message = "You are logged in as %s!" % request.user.username
    form = DMSForm() # Old solution: (user = request.user)
    context = {
        'form': form,
        'switches': list(Switch.objects.filter(controller__user=request.user)),
        'login_message': login_message
    }
    return render(request, 'dms/dashboard-view.html', context)
