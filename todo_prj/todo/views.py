from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

from .models import Task
from django.urls import reverse_lazy

# # functionbased
# def home(request):
#     return HttpResponse("Working")

# classbased
class TaskList(ListView):
    model = Task
    context_object_name = 'task'
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')
class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task")
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy("task")
class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = "__all__"
    redirect_authenticated_user: False

    def get_success_url(self):
        return reverse_lazy('task')