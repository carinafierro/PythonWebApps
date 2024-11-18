from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'