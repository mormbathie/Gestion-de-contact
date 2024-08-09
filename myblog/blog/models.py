from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name =models.CharField(max_length=150)
    lastname =models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=150)
    email = models.EmailField(max_length=150 , null=True , blank=True) 
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    archif = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.lastname}"
