from django import forms


class ProfileForm(forms.Form):
   first_name = forms.CharField(label=" نام خانوادگی خود را وارد کنید" , max_length=25)
   last_name = forms.CharField(label=" نام خانوادگی خود را وارد کنید" , max_length=25)
   phone_number = forms.CharField(label=" شماره تلفن خود را وارد کنید" , max_length=11)
   email_address = forms.CharField(label="ایمیل خود را وارد کنید" , max_length=255)
   national_code = forms.CharField(label= " کد ملی خود را وارد کنید" , max_length=14)


class AddressForm(forms.Form):
   title = forms.CharField(label="عنوان آدرس خود را وارد کنید", max_length = 50)
   recipient_full_name = forms.CharField(label="تام و نام خانوادگی تحویل گیرنده را وارد کنید ", max_length=35)
   state = forms.CharField(label=" نام استان محل زندگی خود را وارد کنید", max_length = 50)
   city = forms.CharField(label="نام شهر محل زندگی خود را وارد کنید", max_length = 50)
   street = forms.CharField(label="نام خیابان محل زندگی خود را وارد کنید", max_length = 50)
   postal_code = forms.CharField(label="کد پستی خود را وارد کنید", max_length = 50)
   building_number = forms.CharField(label="پلاک ساختمان خود را وارد کنید", max_length = 50)
   building_unit_number = forms.CharField(label=" شماره واحد خود را وارد کنید", max_length = 50)