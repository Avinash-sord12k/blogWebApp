from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms  import SignUpForm

class UserCreation(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserEdit(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'userEdit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
