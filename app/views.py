from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Profile

# Create your views here.

def index(request):

    context = {
        "title":"Pagina-Inicial",
    }

    if not request.user.is_authenticated:

        return render(request,'index.html',context)
    else:
        context["title"] = "logged",
        context["user"] =  User.objects.get(username=request.user.username)
    

        return render(request,'logged_index.html',context)