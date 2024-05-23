from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("This is main page")
    return render(request=request, template_name=("photocore/index.html"))

def storage_view(request):
    

    if request.user.is_authenticated:
        userstatus = "Logged in"
    else:
        userstatus = "unlogged"

    data = {
        "userstatus": userstatus,
        "request": request,
        "username": request.user.username,
    }
    return render(request, "photocore/storage.html", data)