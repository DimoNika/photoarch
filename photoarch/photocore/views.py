from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("This is main page")




    data = {
        "is_logged": request.user.is_authenticated,

        "username": request.user.username,
    }
    return render(request, "photocore/index.html", data)

def storage_view(request):


    data = {
        "is_logged": request.user.is_authenticated,
        "request": request,
        "username": request.user.username,
        "test": " | Storage",
    }
    return render(request, "photocore/storage.html", data)