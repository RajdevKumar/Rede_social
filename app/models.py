from django.db import models
from django.contrib.auth.models import User



def fnc(instance,filename):
    return "%s/%s" %(instance.user.username,filename)

GENERO_CHOICES = (
    ("M",("MASCULINO")),
    ("F",("FEMENINO")),
    #("D",("Default")),
)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    Email = models.CharField(max_length=40,unique=True)
    genero = models.CharField(choices=GENERO_CHOICES,max_length=40,null=False,default="D")
    Avatar = models.FileField(upload_to=fnc)
    N_seguidores = models.IntegerField(default=0,null=False)
    N_seguindo = models.IntegerField(default=0,null=False)

