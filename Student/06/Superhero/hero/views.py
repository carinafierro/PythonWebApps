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