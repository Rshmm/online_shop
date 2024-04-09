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
            address_exists = request.user.address_set.exists()
            if address_exists: 
                address = request.user.address_set.first()
                address.title = request.POST.get('title')
                address.recipient_full_name = request.POST.get('recipient_full_name')
                address.state = request.POST.get('state')
                address.city = request.POST.get('city')
                address.street = request.POST.get('street')
                address.postal_code = request.POST.get('postal_code')
                address.building_number = request.POST.get('building_number')
                address.building_unit_number = request.POST.get('building_unit_number')
                address.save()
                messages.add_message(request, messages.SUCCESS ,"اطلاعات با موفقیت ذخیره شد")

            else:
                request.user.address_set.create(
                title = request.POST.get('title'),
                recipient_full_name = request.POST.get('recipient_full_name'),
                state = request.POST.get('state'),
                city = request.POST.get('city'),
                street = request.POST.get('street'),
                postal_code = request.POST.get('postal_code'),
                building_number = request.POST.get('building_number'),
                building_unit_number =  request.POST.get('building_unit_number')
                )

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
            request.user.userprofile.first_name = request.POST.get('first_name')
            request.user.userprofile.last_name = request.POST.get('last_name')
            request.user.userprofile.phone_number = request.POST.get('phone_number')
            request.user.userprofile.email_address = request.POST.get('email_address')
            request.user.userprofile.national_code = request.POST.get('national_code')
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