from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def Profile(request):
    return render(request,'profile.html')

@login_required
def Address(request):
    return render(request,'address.html')

@login_required
def Createaddress(request):
    return render(request,'address-create.html')

@login_required
def Userpanel(request):
    return render(request,'user_panel.html')

@login_required
def edit_user_panel(request):
    return render(request,'edit_user_panel.html')

def Home(request):
    return render(request, 'home.html')