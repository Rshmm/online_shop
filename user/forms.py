from django import forms


class ProfileForm(forms.Form):
   first_name = forms.CharField(label=" نام خانوادگی خود را وارد کنید" , max_length=25,required=True)
   last_name = forms.CharField(label=" نام خانوادگی خود را وارد کنید" , max_length=25,required=True)
   phone_number = forms.CharField(label=" شماره تلفن خود را وارد کنید" , max_length=11,required=True)
   email_address = forms.CharField(label="ایمیل خود را وارد کنید" , max_length=255,required=True)
   national_code = forms.CharField(label= " کد ملی خود را وارد کنید" , max_length=14,required=True)


class AddressForm(forms.Form):
   title = forms.CharField(label="عنوان آدرس خود را وارد کنید", max_length = 50,required=True)
   recipient_full_name = forms.CharField(label="تام و نام خانوادگی تحویل گیرنده را وارد کنید ", max_length=35,required=True)
   state = forms.CharField(label=" نام استان محل زندگی خود را وارد کنید", max_length = 50,required=True)
   city = forms.CharField(label="نام شهر محل زندگی خود را وارد کنید", max_length = 50,required=True)
   street = forms.CharField(label="آدرس کامل محل زندگی خود را وارد کنید", max_length = 50,required=True)
   postal_code = forms.CharField(label="کد پستی خود را وارد کنید", max_length = 50,required=True)
   building_number = forms.CharField(label="پلاک ساختمان خود را وارد کنید", max_length = 50,required=True)
   building_unit_number = forms.CharField(label=" شماره واحد خود را وارد کنید", max_length = 50,required=True)