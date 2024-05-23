from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("This is main page")
    data = {
        
    }
    return render(request, "photocore/index.html", data)

def storage_view(request):
    

    if request.user.is_authenticated:
        userstatus = "Logged in"
    else:
        userstatus = "unlogged"

    data = {
        "userstatus": userstatus,
        "request": request,
        "username": request.user.username,
        "test": " | Storage",
    }
    return render(request, "photocore/storage.html", data)