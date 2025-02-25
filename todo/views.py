from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,  UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo/taskList.html'
    context_object_name = 'tasks'
    login_url = 'signin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        
        context['search_input'] = search_input

        return context
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'todo/task.html'
    context_object_name = 'task'
    login_url = 'signin'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'dua_date']
    template_name = 'todo/addTask.html'
    success_url = reverse_lazy('tasks')
    login_url = 'signin'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'dua_date', 'complete']
    template_name = 'todo/updateTask.html'
    success_url = reverse_lazy('tasks')
    login_url = 'signin'

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo/deleteTask.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    login_url = 'signin'
