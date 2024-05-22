from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("This is main page")
    return render(request=request, template_name=("photocore/index.html"))

def storage_view(request):
    return render(request=request, template_name=("photocore/storage.html"))