from django.db import models

# Create your models here.


class Todo(models.Model):
    nev = models.CharField(max_length=30)
    leiras = models.TextField(null=True, blank=True)
    allapot = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
