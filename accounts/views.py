from django.shortcuts import render
from .models import Usuario
from .utils import loginValidate


def login(request):

    return render(request, "login/index.html")


def listUsers(request):
    users = Usuario.objects.all()

    return render(request, "login/list.html", {"usuarios": users})
