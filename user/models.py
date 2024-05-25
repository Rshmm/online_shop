from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


User = get_user_model()

# user = User.objects.last()
# user.Address_set.all()

class UserProfile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)


    first_name=models.CharField(
        null=True,
        max_length=25,
        default=""
        # validators=[
        #     RegexValidator(
        #         regex='^[a-zA-Z]$',
        #         message="Enter a valid registration first_name in the format a-z A-Z"
        #     )
        # ]
        )
    

    last_name=models.CharField(
        null=True,
        max_length=25,
        default=""
        # validators=[
        #         RegexValidator(
        #             regex='^[a-zA-Z]$',
        #             message="Enter a valid last_name in the format a-z A-Z"
        #     )
        # ]
        )
    

    phone_number=models.CharField(
        max_length=11,
        null=True,
        default=""
        # validators=[
        #         RegexValidator(
        #             regex='^[0-9]$',
        #             message="Enter a valid registration phone number in the format 09XXXXXXXXX"
        #     )
        # ]
        )
    
    email_address=models.CharField(null=True,max_length=255,default="")


    national_code = models.CharField(null=True,max_length=14,default="")


class Address(models.Model):

    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    title=models.CharField(null=True,max_length=50)
    recipient_full_name=models.CharField(
        null=True,
        max_length=35,
        # validators=[
        #     RegexValidator(
        #         regex='^[a-zA-Z]$',
        #         message="Enter a valid  first_name in the format a-z A-Z"
        #     )
        # ]
        )
    state=models.CharField(null=True,max_length=50)
    city=models.CharField(null=True,max_length=50)
    full_address=models.CharField(null=True,max_length=500)
    postal_code=models.CharField(
        null=True,
         max_length = 50,
        # validators=[
        #         RegexValidator(
        #             regex='^[0-9]$',
        #             message="Enter a valid  postal code with numbers between 0-9"
        #     )
        # ]
        )
    building_number=models.CharField(
        null=True,
         max_length = 50,
        #  validators=[
        #         RegexValidator(
        #             regex='^[0-9]$',
        #             message="Enter a valid  building_number with numbers between 0-9"
        #     )
        # ]
        )
        
    building_unit_number=models.CharField(
        null=True,
        max_length = 50,
        #  validators=[
        #         RegexValidator(
        #             regex='^[0-9]$',
        #             message="Enter a valid building_unit_number with numbers between 0-9"
        #     )
        # ]
        )
        