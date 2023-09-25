from django.contrib import admin
from . models import Programmer, Project

admin.site.register((Project,Programmer))
