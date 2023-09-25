from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .models import Programmer, Project



class IndexView(generic.ListView):
    template_name = 'main_app/index.html'
    context_object_name = "programmer_list"

    def get_queryset(self):
        return Programmer.objects.all()
    

class ProgrammerDetailView(generic.DetailView):
    model = Programmer
    template_name = 'main_app/concret_programmer.html'


def add_programmer(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password = request.POST["password"]
        age = request.POST["age"]
        language = request.POST["language"]
        framework = request.POST["framework"]
        experience = request.POST["experience"]

        user = User.objects.create_user(username = fname, first_name = fname, last_name = lname, password = password)
        user.save()

        programmer = Programmer(user = user, age = age, language = language, framework = framework, experience = experience)
        programmer.save()

        return redirect('http://localhost:8000/')
    
    return render(request, "main_app/add_programmer.html")

