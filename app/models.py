from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def fnc(instance,name):
    return "%s/%s" %(instance,name)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    Email = models.CharField(max_length=40,unique=True)
    genero = models.CharField(max_length=40,null=False,default="Não Identificado")
    Avatar = models.FileField(upload_to=fnc)
    N_seguidores = models.IntegerField(default=0,null=False)
    N_seguindo = models.IntegerField(default=0,null=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()