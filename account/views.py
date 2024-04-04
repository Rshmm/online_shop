from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    # def form_valid(self, form):
    #     valid = super().form_valid(form)
    #     username, password = form.cleaned_data('username'), form.cleaned_data('password')
    #     new_user = authenticate(username=username, password=password)
    #     login(self.request, new_user)
    #     return valid