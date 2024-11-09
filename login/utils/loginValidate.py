from django.shortcuts import redirect
from models import Usuario
from login import views


def loginValidate(userName, password):

    user = Usuario.objects.get(name="Pablo")
    usPass = Usuario.objects.get(lastName="Aquise")

    # if userName == user:
    #    if password ==
