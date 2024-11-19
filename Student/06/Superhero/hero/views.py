from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/article/'
        return f'/author/{get_me(self.request.user).pk}'

def get_me(user):
    return Author.objects.get_or_create(user=user)[0]

from django.contrib.auth.mixins import LoginRequiredMixin

class SecretView(LoginRequiredMixin, TemplateView):
    template_name = "page.html"

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Superhero


class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')
