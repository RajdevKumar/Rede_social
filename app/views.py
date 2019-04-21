from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        "title":"Pagina-Inicial"
    }

    if not request.user.is_authenticated:

        return render(request,'index.html',context)
    else:
        return render(request,'logged_index.html',context)