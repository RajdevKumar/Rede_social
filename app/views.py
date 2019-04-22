from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Profile
from .forms import UserForm, ProfileForm

# Create your views here.

def index(request):

    context = {
        "title":"Pagina-Inicial",
    }

    if not request.user.is_authenticated:

        user_form = UserForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None)
        if user_form.is_valid() and profile_form.is_valid():
            #print(request.POST.get('username'))
            # Cria Usuario
            Username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]
            pn = user_form.cleaned_data["first_name"]
            ln = user_form.cleaned_data["last_name"]
            gender = profile_form.cleaned_data["genero"]
        else:
            print("ERRO")

        context["user_form"] = user_form
        context["profile_form"] = profile_form
        return render(request,'index.html',context)
    else:
        context["title"] = "logged",
        context["user"] =  User.objects.get(username=request.user.username)
    

        return render(request,'logged_index.html',context)