from django.core.mail import EmailMessage, send_mail

def activateDMS(switch):
    pass

def sendNotification(switch):
    # email = EmailMessage(
    #     'Alert: Your Dead Mans Switch activates in %d days!' % switch.notification,
    #     'Click on this link, if you dont want it to activate.',
    #     to=[merlin.buczek@gmail.com]
    # )
    # email.send()
    print('Alert send to ', switch.controller.user.email)#.controller.user.email)
    send_mail(
        'Alert: Your Dead Mans Switch activates in %d days!' % switch.notification,
        'Click on this link, if you dont want it to activate.',
        'info@inherabit.com',
        [switch.controller.user.email],
        fail_silently=False,
    )
    send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
