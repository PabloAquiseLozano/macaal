from django.db import models

# Create your models here.


class Usuario(models.Model):

    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    carreer = models.TextField()

    class Meta:
        db_table = "usuarios"
