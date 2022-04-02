from tkinter import Widget
from django import forms
from .models import TakingTimeAlarm, MedicineMangement, CompanyMedicineName, Item, MedicineRegister
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput, TimePickerInput


class TimeSettingForm(forms.ModelForm):
    class Meta:
        model = TakingTimeAlarm
        fields = '__all__'


class ManagementTopForm(forms.ModelForm):
    class Meta:
        model = MedicineMangement
        fields = '__all__'
        widgets = {
            'medicine_name': forms.Select(attrs={'class': 'form-select'}),
            'taking_start': DateTimePickerInput(options={
                'format': 'YYYY/MM/DD HH:mm',
                'locale': 'ja',
            })
        }


class CompanyMedicineNameForm(forms.ModelForm):
    class Meta:
        model = CompanyMedicineName
        fields = ['medicine_name', 'company_name', 'initials']
        lavels = {'medicine_name': '薬名',
                  'company_name': '会社名', 'initials': '頭文字'}


class MedicineRegisterForm(forms.ModelForm):
    class Meta:
        model = MedicineRegister
        fields = ['kinds', 'dosage_form']
        widgets = {
            'kinds': forms.Select(attrs={'class': 'form-select'}),
            'dosage_form': forms.Select(attrs={'class': 'form-select'}),
        }
