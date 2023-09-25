from django.db import models
from django.contrib.auth.models import User


class Programmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    language = models.CharField(max_length=75)
    framework = models.CharField(max_length=75)
    experience = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.user.username


class Project(models.Model):
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.name
