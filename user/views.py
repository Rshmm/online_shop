from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.forms import ProfileForm, AddressForm
from user.models import UserProfile,Address
from django.contrib import messages
from user.models import User


@login_required
def Profile(request):
    return render(request,'profile.html')

@login_required
def Address(request):
    return render(request,'address.html')

@login_required
def Createaddress(request):
    
    if request.method == "POST":
        Createaddressform = AddressForm(request.POST)
        # check whether it's valid:
        if Createaddressform.is_valid():

            address = request.user.address_set.first()
            address.title = request.Post.get('title')
            address.recipient_full_name = request.Post.get('recipient_full_name')
            address.state = request.Post.get('state')
            address.city = request.Post.get('city')
            address.street = request.Post.get('street')
            address.postal_code = request.Post.get('postal_code')
            address.building_number = request.Post.get('building_number')
            address.building_unit_number = request.Post.get('building_unit_number')
            address.save()
            messages.add_message(request, messages.SUCCESS ,"اطلاعات با موفقیت ذخیره شد")

        else:
            messages.add_message(request, messages.ERROR ,"مشکلی وجود دارد به ارور توجه کنید یا لطفا تمامی فرم هارا پر کنید")


    else:
        Createaddressform = AddressForm()
    return render(request,'address-create.html', {
        'Createaddressform': Createaddressform
    })

@login_required
def Userpanel(request):
    return render(request,'user_panel.html')

@login_required
def edit_user_panel(request):
    

    if request.method == "POST":
        edituserpanelform = ProfileForm(request.POST)
        if edituserpanelform.is_valid():
            request.user.userprofile.first_name = edituserpanelform.cleaned_data['first_name']
            request.user.userprofile.last_name = edituserpanelform.cleaned_data['last_name']
            request.user.userprofile.phone_number = edituserpanelform.cleaned_data['phone_number']
            request.user.userprofile.email_address = edituserpanelform.cleaned_data['email_address']
            request.user.userprofile.national_code = edituserpanelform.cleaned_data['national_code']
            request.user.userprofile.save()
            messages.add_message(request, messages.SUCCESS ,"اطلاعات با موفقیت ذخیره شد")
        
        else:
            messages.add_message(request, messages.ERROR ,"مشکلی وجود دارد به ارور توجه کنید یا لطفا تمامی فرم هارا پر کنید")


    else:
        edituserpanelform = ProfileForm(initial=request.user.userprofile.__dict__)
    return render(request,'edit_user_panel.html', {
        'edituserpanelform': edituserpanelform
    })

def Home(request):
    return render(request, 'home.html')