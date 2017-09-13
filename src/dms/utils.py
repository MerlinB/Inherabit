from django.core.mail import EmailMessage, send_mail
from .models import Switch
from datetime import date #, timedelta


def checkDays():
    now = date.today()
    for s in Switch:
        dayspassed = (now - s.controller.last_seen).days
        if dayspassed >= s.timeframe:
            activateDMS(s)
        elif dayspassed + s.notification is s.timeframe:
            sendNotification(s)


def activateDMS(switch):
    print("Activating DMS for ", s.controller.user.username)


def resetTimer(user):
    user.controller.last_seen = date.today()


def sendNotification(switch):
    send_mail(
        'Alert: Your Dead Mans Switch activates in %d days!' % switch.notification,
        'Log in at Inherabit.com to reset it.',
        'info@inherabit.com',
        [switch.controller.user.email],
        fail_silently=False,
    )
    # TODO: Check for failure, handle it.
    print('Alert send to ', switch.controller.user.email)
