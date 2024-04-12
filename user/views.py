from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory 
from user.forms import ProfileForm, AddressForm
from user.models import UserProfile,Address
from django.contrib import messages
from user.models import User
from django.core import serializers
from user.helpers import get_form_set_key,get_form_set_value

@login_required
def Profile(request):
    return render(request,'profile.html')

@login_required
def Address(request):
    return render(request,'address.html')




@login_required 
def Createaddress(request):
        CreateaddressFormSet= formset_factory(AddressForm)
        if request.method == "POST":
            # Createaddressformset = CreateaddressFormSet(request.POST)
            from_set_indexes = get_form_set_key(request)
            request.user.address_set.all().delete()
            for key in from_set_indexes:
                address_data = get_form_set_value(request, key)
                request.user.address_set.create(**address_data)
                messages.add_message(request, messages.SUCCESS ,"اطلاعات با موفقیت ذخیره شد")

            # else:
            #     messages.add_message(request, messages.ERROR ,"مشکلی وجود دارد به ارور توجه کنید یا لطفا تمامی فرم هارا پر کنید")
           

            # if Createaddressformset.is_valid():



        else:
            adrs = request.user.address_set.first()
            data = adrs.__dict__ if adrs else {}
            # Createaddressform = AddressForm(initial=data)  
            Createaddressformset = CreateaddressFormSet(
                initial=[adrs.__dict__ for adrs in request.user.address_set.all()]
            ) 
        return render(request,'address-create.html', {
            # 'Createaddressformset': Createaddressformset,
            'address_set' :serializers.serialize('json' ,request.user.address_set.all())
            
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

