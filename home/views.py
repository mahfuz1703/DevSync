from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

class loginView(LoginView):
    template_name = 'home/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password!!")
        return super().form_invalid(form)
    
class registerView(FormView):
    template_name = 'home/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('tasks')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('c-password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, self.template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, self.template_name)

        user = User.objects.create_user(username=username, password=password)
        user.save()

        login(request, user)

        return redirect('tasks')