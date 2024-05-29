from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFilesForm
from .models import UploadFile
from django.urls import reverse
import os
# Create your views here.

# Custom func for extention of files
def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension

def index(request):
    # return HttpResponse("This is main page")




    data = {
        "is_logged": request.user.is_authenticated,

        "username": request.user.username,
    }
    return render(request, "photocore/index.html", data)

def storage_view(request):
    
    if request.method == "POST":

        allowed_extensions = ['.bmp', '.gif', '.jpg', '.jpeg', '.png', '.webp','.mp4', '.webm',  '.ogg']

        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():            
            # Iterate over the files in the request
            for f in request.FILES.getlist('file'):
            
                # Check if file is allowed
                if any(f.name.endswith(ext) for ext in allowed_extensions):
                    # Save each file individually
                    fp = UploadFile(file=f, owner=request.user)
                    fp.save()
        return HttpResponseRedirect(reverse("storage"))

    files =  UploadFile.objects.filter(owner=request.user, is_deleted=False),
    files_with_types = []
    

    for i in files:
    
        for j in i:

            if get_file_extension(str(j.file)) in ['.bmp', '.gif', '.jpg', '.jpeg', '.png', '.webp']:
                files_with_types.append((j, "picture"))
            elif get_file_extension(str(j.file)) in [".mp4", ".webm",  ".ogg"]:
                files_with_types.append((j, "video"))
            else:
                files_with_types.append((j, "unknown"))
    
                
                # ['.bmp', '.gif', '.jpg', '.jpeg', '.png', '.webp'];
                # [".mp4", ".webm",  ".ogg"]
            
    data = {
        "files_with_types": files_with_types,
        "files" : UploadFile.objects.filter(owner=request.user, is_deleted=False),
        "is_logged": request.user.is_authenticated,
        "request": request,
        "username": request.user.username,
        "form": UploadFilesForm(),
        "test": " | Storage",
    }
    return render(request, "photocore/storage.html", data)