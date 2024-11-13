from django.db import models
from django.utils import timezone

# Create your models here.


class Usuario(models.Model):

    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(default="")
    carreer = models.TextField(default="")
    userPass = models.TextField(default="")
    isDeleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"
