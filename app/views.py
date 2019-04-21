from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        "title":"Pagina-Inicial"
    }

    return render(request,'index.html',context)