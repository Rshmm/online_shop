from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from account.helper.decorators import create_view_logout_required


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    
    def get_success_url(self, **kwargs):
        next_page = self.request.GET.get('next')
        if next_page:
            return next_page
        return '/'

    @create_view_logout_required('/')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
   

    @create_view_logout_required('/')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

    def form_valid(self, form):
        valid = super().form_valid(form)
        username, password = form.cleaned_data['username'], form.cleaned_data['password1']
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


    