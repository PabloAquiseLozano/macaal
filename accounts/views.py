from django.shortcuts import render
from .models import Usuario
from .utils import loginValidate


def login(request):

    return render(request, "login/index.html")
