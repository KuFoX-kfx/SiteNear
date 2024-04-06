from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def login_page(request):
    return render(request, 'user/login_page.html')

def register_page(request):
    return render(request, 'user/register_page.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
    
def home(request):
    return render(request,"users/home.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Создан аккаунт {username}!')
        return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})