from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Controller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='controller')

@receiver(post_save, sender=User)
def create_user_controller(sender, instance, created, **kwargs):
    if created:
        Controller.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_controller(sender, instance, **kwargs):
    #if hasattr(instance, 'controller'): # NOT WORKING
        instance.controller.save()
    # else:
    #     print("No Controller!")


class Switch(models.Model):
    timeframe = models.IntegerField()
    dayspassed = models.IntegerField(default=0)
    notification = models.IntegerField(default=20)
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE)
