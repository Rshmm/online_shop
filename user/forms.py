from django import forms


class ProfileForm(forms.Form):
   def __init__(self,*args, **kwargs):
      if 'initail' in kwargs: 
         if kwargs['initial']['first_name'] == '':
            kwargs['initial']['first_name'] == ''
         if kwargs['initial']['last_name'] == '':
            kwargs['initial']['last_name'] == ''
         if kwargs['initial']['phone_number'] == '':
            kwargs['initial']['phone_number'] == ''
         if kwargs['initial']['email_address'] == '':
            kwargs['initial']['email_address'] ==''
         if kwargs['initial']['national_code'] == '':
            kwargs['initial']['national_code'] ==''
      super().__init__(*args, **kwargs)
      

   first_name = forms.CharField(label=" نام خانوادگی خود را وارد کنید",
                                max_length=25,
                                required=True,
                                widget=forms.TextInput(attrs={"class":"form-control"})
                                )

   last_name = forms.CharField(label=" نام خانوادگی خود را وارد کنید",
                                max_length=25,
                                required=True,
                                widget=forms.TextInput(attrs={"class":"form-control"})
                                )

   phone_number = forms.CharField(label=" شماره تلفن خود را وارد کنید",
                                max_length=11,
                                required=True,
                                widget=forms.TextInput(attrs={"class":"form-control"})
                                )

   email_address = forms.EmailField(label="ایمیل خود را وارد کنید",
                                max_length=255,
                                required=True,
                                widget=forms.TextInput(attrs={"class":"form-control"})
                                )

   national_code = forms.CharField(label= " کد ملی خود را وارد کنید",
                                max_length=14,
                                required=True,
                                widget=forms.TextInput(attrs={"class":"form-control"})
                                )



class AddressForm(forms.Form):
   title = forms.CharField(label="عنوان آدرس خود را وارد کنید",
                           max_length = 50,
                           required=True,
                           widget=forms.TextInput(attrs={"class":"form-control"})
                           )

   recipient_full_name = forms.CharField(label="تام و نام خانوادگی تحویل گیرنده را وارد کنید ",
                           max_length=35,
                           required=True,
                           widget=forms.TextInput(attrs={"class":"form-control"})
                           )

   state = forms.CharField(label=" نام استان محل زندگی خود را وارد کنید",
                           max_length = 50,
                           required=True,
                           widget=forms.Textarea(attrs={
                              "class":"form-control"
                              }
                              )
                           )

   city = forms.CharField(label="نام شهر محل زندگی خود را وارد کنید",
                           max_length = 50,
                           required=True,
                           widget=forms.TextInput(attrs={"class":"form-control"})
                           )

   street = forms.CharField(label="آدرس کامل محل زندگی خود را وارد کنید",
                           max_length = 50,
                           required=True,
                           widget=forms.TextInput(attrs={"class":"form-control"})
                           )

   postal_code = forms.CharField(label="کد پستی خود را وارد کنید",
                           max_length = 50,
                           required=True,
                           widget=forms.TextInput(attrs={"class":"form-control"})
                           )

   building_number = forms.CharField(label="پلاک ساختمان خود را وارد کنید",
                           max_length = 50,
                           required=True,
                           widget=forms.TextInput(attrs={"class":"form-control"})
                           )

   building_unit_number = forms.CharField(label=" شماره واحد خود را وارد کنید",
                           max_length =50 ,
                           widget=forms.TextInput(attrs={"class":"form-control"}),
                           required=True
                           )