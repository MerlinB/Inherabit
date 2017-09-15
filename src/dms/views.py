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
    switches = Switch.objects.filter(controller__user=request.user)
    if request.method == 'POST':
        # if(request.GET.get('mybtn')):
        #     form = DMSForm(request.POST)
        # else:
        if int(request.POST['notification']) > int(request.POST['timeframe']):
            print(request.POST['notification'],request.POST['timeframe'])
            messages.error(request, "Notification can't be bigger than the timeframe.")
        else:
            # current = switches.get(id=request.POST['switch'])
            if 'switch' in request.POST:
                form = DMSForm(request.POST, instance=switches.get(id=request.POST['switch']))
                if form.is_valid():
                    form.save()
                    messages.info(request, 'DMS changed.')
            else:
                form = DMSForm(request.POST)
                if form.is_valid():
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
        #os.system('(crontab -l ; echo "0 4 * * * myscript")| crontab') # Nicht gut, um cronjob nicht zuzuspammen.
    resetTimer(request.user)
    # form = DMSForm() # Old solution: (user = request.user)
    context = {
        # 'form': form,
        'switches': list(switches),
        'empty_cards': range(10),
    }
    if(request.GET.get('edit')):
        print("Modal: Edit button",request.GET.get('switch'))
        switch = switches.get(id=request.GET.get('switch'))
        # context['edit'] = request.GET.get('switch')
        context['form'] = DMSForm(instance=switch)
        context['submit'] = 'Save Changes'
        context['formtitle'] = 'Edit Switch'
        context['switch'] = switch
    elif(request.GET.get('new')):
        print("Modal: New Button")
        context['form'] = DMSForm()
        context['submit'] = 'Create Switch'
        context['formtitle'] = 'Create new Switch'
    return render(request, 'dms/dashboard-view.html', context)
