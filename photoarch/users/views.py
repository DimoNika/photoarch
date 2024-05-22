from django.shortcuts import render
from .forms import LoginUserForm

# Create your views here.

def login(request):
    # return HttpResponse("This is main page")
    form = LoginUserForm()




    return render(request, "users/login.html", {"form": form})