from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE )
    name = models.CharField(max_length=120, null=True, blank=False)
    phone = models.CharField(max_length=120, null=True, blank=False)
    email = models.CharField(max_length=120, null=True, blank=False)
    profile_pic = models.ImageField(default="profile_photo.png", null=True, blank=True)

class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE )
    name = models.CharField(max_length=120, null=True, blank=False)
    phone = models.CharField(max_length=120, null=True, blank=False)
    email = models.CharField(max_length=120, null=True, blank=False)
    profile_pic = models.ImageField(default="profile_photo.png", null=True, blank=True)

# Create your models here.
