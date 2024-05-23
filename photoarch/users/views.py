from django.shortcuts import render
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import MyRegistreForm
# Create your views here.

def login_view(request):
    # return HttpResponse("This is main page")
    # return HttpResponse("hello world")
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"],
                                password=cd["password"])
            if user and user.is_active:
                # auth.login(request=request, user=user)
                login(request, user)    
                return HttpResponseRedirect(reverse("storage"))
            else:
                return render(request, "users/login.html", {"form": form})
    else:
        form = LoginUserForm()
    
    return render(request, "users/login.html", {"form": form})




def registre_view(request):
    
    if request.method == "POST":
        form = MyRegistreForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:login"))
        else:
            pass
            
           
    else:
        form = MyRegistreForm()
        # form = form.
    # print(form.media)
    return render(request, "users/registre.html", {"form": form})