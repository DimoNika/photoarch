from django.shortcuts import render
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import MyRegistreForm
# Create your views here.

def login_view(request):
    # return HttpResponse("This is main page")
    # return HttpResponse("hello world")
    if request.user.is_authenticated:  # If user alredy refistered redirect to storage
        return HttpResponseRedirect(reverse("storage"))
    else:
        pass



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
                data = {
                    "form": form,
                    "test": " | Login",
                }
                return render(request, "users/login.html", data)
    else:
        form = LoginUserForm()
    data = {
        "form": form,
        "test": " | Login",
    }
    return render(request, "users/login.html", data)




def registre_view(request):
    
    if request.user.is_authenticated:  # If user alredy refistered redirect to storage
        return HttpResponseRedirect(reverse("storage"))
    else:
        pass

    if request.method == "POST":
        form = MyRegistreForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:login"))
        else:
            pass
            
           
    else:
        form = MyRegistreForm()
        

        
    data = {
        "form": form,
        "test": " | Registration",
    }
    return render(request, "users/registre.html", data)


def logout_view(request):
    
    logout(request)
    return HttpResponseRedirect(reverse("home"))