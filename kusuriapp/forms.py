from django import forms
from .models import TakingTimeAlarm, MedicineMangement, CompanyMedicineName


class TimeSettingForm(forms.ModelForm):
    class Meta:
        model = TakingTimeAlarm
        fields = '__all__'


class ManagementTopForm(forms.ModelForm):
    class Meta:
        model = MedicineMangement
        fields = '__all__'


class CompanyMedicineNameForm(forms.ModelForm):
    class Meta:
        model = CompanyMedicineName
        fields = ['medicine_name', 'company_name', 'initials']
        lavels = {'medicine_name': '薬名',
                  'company_name': '会社名', 'initials': '頭文字'}
