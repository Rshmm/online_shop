from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.forms import ProfileForm, AddressForm
from user.models import UserProfile,UserAddress
from django.contrib import messages



@login_required
def Profile(request):
    return render(request,'profile.html')

@login_required
def Address(request):
    return render(request,'address.html')

@login_required
def Createaddress(request):
    
    if request.method == "POST":
        form = AddressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            address = UserAddress.objects.get(user=request.user)
            address.title = form.cleaned_data['title']
            address.recipient_full_name = form.cleaned_data['recipient_full_name']
            address.state = form.cleaned_data['state']
            address.city = form.cleaned_data['city']
            address.street = form.cleaned_data['street']
            address.postal_code = form.cleaned_data['postal_code']
            address.building_number = form.cleaned_data['building_number']
            address.building_unit_number = form.cleaned_data['building_unit_number']
            address.save()
            messages.add_message(request, messages.SUCCESS ,"اطلاعات با موفقیت ذخیره شد")

        else:
            messages.add_message(request, messages.ERROR ,"لطفا فرم هارا پر کنید")


    else:
        form = AddressForm()
    return render(request,'address-create.html', {
        'form': form
    })

@login_required
def Userpanel(request):
    return render(request,'user_panel.html')

@login_required
def edit_user_panel(request):
    

    if request.method == "POST":
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            request.user.userprofile.first_name = form.cleaned_data['first_name']
            request.user.userprofile.last_name = form.cleaned_data['last_name']
            request.user.userprofile.phone_number = form.cleaned_data['phone_number']
            request.user.userprofile.email_address = form.cleaned_data['email_address']
            request.user.userprofile.national_code = form.cleaned_data['national_code']
            request.user.userprofile.save()
            messages.add_message(request, messages.SUCCESS ,"اطلاعات با موفقیت ذخیره شد")
        
        else:
            messages.add_message(request, messages.ERROR ,"لطفا فرم هارا پر کنید")


    else:
        form = ProfileForm()
    return render(request,'edit_user_panel.html', {
        'form': form
    })

def Home(request):
    return render(request, 'home.html')