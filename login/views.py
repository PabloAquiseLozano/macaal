from django.shortcuts import render
import sqlite3
from .models import Usuario

# Create your views here.


def login(request):
    return render(request, "login/index.html")


def listUsers(request):
    users = Usuario.objects.all()

    return render(request, "login/list.html", {"usuarios": users})
