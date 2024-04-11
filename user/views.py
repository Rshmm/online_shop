from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory 
from user.forms import ProfileForm, AddressForm
from user.models import UserProfile,Address
from django.contrib import messages
from user.models import User
from django.core import serializers

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
            Createaddressformset = CreateaddressFormSet(request.POST)

            if Createaddressformset.is_valid():
                request.user.address_set.all().delete()
                for form in Createaddressformset:
                    request.user.address_set.create(
                    title = form.cleaned_data.get('title'),
                    recipient_full_name = form.cleaned_data.get('recipient_full_name'),
                    state = form.cleaned_data.get('state'),
                    city = form.cleaned_data.get('city'),
                    street = form.cleaned_data.get('street'),
                    postal_code = form.cleaned_data.get('postal_code'),
                    building_number = form.cleaned_data.get('building_number'),
                    building_unit_number =  form.cleaned_data.get('building_unit_number')
                    )
                    messages.add_message(request, messages.SUCCESS ,"اطلاعات با موفقیت ذخیره شد")

            else:
                messages.add_message(request, messages.ERROR ,"مشکلی وجود دارد به ارور توجه کنید یا لطفا تمامی فرم هارا پر کنید")


        else:
            adrs = request.user.address_set.first()
            data = adrs.__dict__ if adrs else {}
            # Createaddressform = AddressForm(initial=data)  
            Createaddressformset = CreateaddressFormSet(
                initial=[adrs.__dict__ for adrs in request.user.address_set.all()]
            ) 
        return render(request,'address-create.html', {
            'Createaddressformset': Createaddressformset,
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

