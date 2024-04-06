from django import forms


class ProfileForm(forms.Form):
   first_name = forms.CharField(label=" نام خانوادگی خود را وارد کنید" , max_length=25)
   last_name = forms.CharField(label=" نام خانوادگی خود را وارد کنید" , max_length=25)
   phone_number = forms.CharField(label=" شماره تلفن خود را وارد کنید" , max_length=11)
   email_address = forms.CharField(label="ایمیل خود را وارد کنید" , max_length=255)
   national_code = forms.CharField(label= " کد ملی خود را وارد کنید" , max_length=14)