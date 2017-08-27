from django.core.management.base import BaseCommand
from dms.models import Switch
from dms.utils import activateDMS, sendNotification

class Command(BaseCommand):
    help = 'Checks if timeframe is completed.'

    def handle(self, *args, **options):
        for switch in Switch.objects.all():
            if (switch.timeframe - switch.dayspassed) <= 0:
                activateDMS(swtich)
            if (switch.timeframe - switch.dayspassed) == switch.notification:
                print('Sending alert:')
                sendNotification(switch)
            #switch.dayspassed += 1
            switch.save()
