from sqlite3 import complete_statement
from venv import create
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task (models.Model):
    user=models.CharField(max_length=40)
    title=models.CharField(max_length=100)
    description=models.TextField(null=True,blank= True)
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)
    





    