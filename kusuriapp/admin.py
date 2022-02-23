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
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from kusuriapp.models import Kusuri_Data
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
class CompanyMedicineNameResource(resources.ModelResource):
    company_id = Field(attribute='company_id' ,column_name='company_id')
    company_name = Field(attribute='company_name', column_name='company_name')
    medicine_id = Field(attribute='medicine_id', column_name='medicine_id')
    medicine_name = Field(attribute='medicine_name', column_name='medicine_name')
    initials = Field(attribute='initials', column_name='initials')
    
    class Meta:
        model = CompanyMedicineName
        skip_unchanged = True
        use_bulk = True

class CompanyMedicineNameAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display = ('company_id', 'company_name', 'medicine_id','medicine_name', 'initials')
    resource_class = CompanyMedicineNameResource
  
# Register your models here. 
admin.site.register(User, MyUserAdmin)
admin.site.register(MedicineMangement)
admin.site.register(MedicineNameManagement)
admin.site.register(TakingTimeAlarm)
admin.site.register(TakingDosage)
admin.site.register(MedicineRegister)
admin.site.register(CompanyMedicineName)
