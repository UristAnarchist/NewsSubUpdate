from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm, SignOutForm


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


class SignOut(CreateView):
    model = User
    form_class = SignOutForm
    success_url = '/accounts/logout'
    template_name = 'registration/logout.html'
