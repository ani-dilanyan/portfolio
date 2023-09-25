from django.shortcuts import render
from django.http import HttpResponse


from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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
