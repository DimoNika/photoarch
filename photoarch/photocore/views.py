from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFilesForm
from .models import UploadFile
from django.urls import reverse
# Create your views here.


def index(request):
    # return HttpResponse("This is main page")




    data = {
        "is_logged": request.user.is_authenticated,

        "username": request.user.username,
    }
    return render(request, "photocore/index.html", data)

def storage_view(request):
    
    if request.method == "POST":
        
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():            
            # Iterate over the files in the request
            for f in request.FILES.getlist('file'):
                # Save each file individually
                fp = UploadFile(file=f, owner=request.user)
                fp.save()
        return HttpResponseRedirect(reverse("storage"))

    data = {
        "files" : UploadFile.objects.filter(owner=request.user, is_deleted=False),
        "is_logged": request.user.is_authenticated,
        "request": request,
        "username": request.user.username,
        "form": UploadFilesForm(),
        "test": " | Storage",
    }
    return render(request, "photocore/storage.html", data)