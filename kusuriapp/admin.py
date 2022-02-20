import pandas as pd
import dask
import dask.dataframe as dd
from dask.delayed import delayed
import sqlite3
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User
from .models import MedicineMangement
from .models import MedicineNameManagement
from .models import TakingTimeAlarm
from .models import TakingDosage
from .models import MedicineRegister
from .models import CompanyMedicineName

Data = pd.read_excel( "./link/ all.xlsx" ,sheet_name = "" )

aaaaa = dask.delayed(pd.read_excel)( "./link/ all.xlsx" ,sheet_name = "" )
Data = dd.from_delayed( aaaaa ).compute()

conn = sqlite3.connect( "会社薬リスト.db" )
conn.close()
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
  
  
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
  
  
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
  
# Register your models here. 
admin.site.register(User, MyUserAdmin)
admin.site.register(MedicineMangement)
admin.site.register(MedicineNameManagement)
admin.site.register(TakingTimeAlarm)
admin.site.register(TakingDosage)
admin.site.register(MedicineRegister)
admin.site.register(CompanyMedicineName)
