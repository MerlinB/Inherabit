from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Controller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='controller')
    last_seen = models.DateField(auto_now_add=True)

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
    name = models.CharField(default="New Switch", max_length=50)
    timeframe = models.IntegerField()
    notification = models.IntegerField()
    beneficiary = models.EmailField()
    secret = models.TextField(blank=True, null=True)
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE)
    
    def __str__(self):
        return (str(self.id) + " | " + self.controller.user.username + ": TF:" + str(self.timeframe) + " | N:" + str(self.notification))
    
    
