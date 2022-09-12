import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task

# # functionbased
# def home(request):
#     return HttpResponse("Working")

# classbased
class TaskList(ListView):
    model = Task
    context_object_name = 'task'