# Rede_social

Conta superUser criada:
#
## ID : rajdevkumar 
## senha : 123

#

## APPS
#
App, app é utilizado como o app 'core' do projeto.
Por isto ele também possui o modelo users extendido

#

## Obter Email do usuario

from django.contrib.auth.models import User
##
u = User.objects.get(username="rajdevkumar")
#
u.profile.Email = email
#
u.save()
