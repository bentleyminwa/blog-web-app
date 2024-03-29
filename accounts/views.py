from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

from django.urls import reverse_lazy


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'