from typing import Any
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from user.models import *


User = get_user_model()


class ProfileInLine(admin.StackedInline):
    model = UserProfile


class AddressInLine(admin.StackedInline):
    model = UserAddress
    extra = 0



class UserAdmin(DjangoUserAdmin):
    inlines=[ProfileInLine,AddressInLine]



    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request,obj)  
        normal_user_fieldsets = (
            (None, {"fields": ("username", "password")}),
        )
        return fieldsets if request.user.is_superuser else normal_user_fieldsets

    
    def get_queryset(self, request):
        qs =  super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(id=request.user.id)
            

admin.site.unregister(User)
admin.site.register(User , UserAdmin)