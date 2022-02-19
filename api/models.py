from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.



class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, null=True, blank=True,unique=True)

    class Meta:
        db_table = "CustomUser"

class Snippet(models.Model):
    title  = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey('CustomUser',on_delete=models.SET_NULL,null=True,blank=True,related_name="createdby")
    tag = models.ForeignKey('Tag',on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        db_table = "Snippet"


class Tag(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)

    class Meta:
        db_table = "Tag"
