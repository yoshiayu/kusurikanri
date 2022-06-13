""""""
from tkinter import Widget
from django import forms
from .models import TakingTimeAlarm, MedicineMangement, CompanyMedicineName, Item, MedicineRegister, TakingDosage
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput, TimePickerInput


class TimeSettingForm(forms.ModelForm):

    class Meta:
        model = TakingTimeAlarm
        fields = '__all__'


class MedicineMangementForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicine'].choices = [
            ("", "薬名")] + list(self.fields['medicine'].choices)[1:]

    class Meta:
        model = MedicineMangement
        fields = {'medicine', 'name'}
        widgets = {
            'medicine': forms.Select(attrs={'class': 'form-select'}),
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
    """_summary_

    Args:
        forms (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kinds'].choices = [
            ("", "種別")] + list(self.fields['kinds'].choices)[1:]
        self.fields['dosage_form'].choices = [
            ("", "剤型")] + list(self.fields['dosage_form'].choices)[1:]

    class Meta:
        model = MedicineRegister
        fields = ['kinds', 'dosage_form']
        widgets = {
            'kinds': forms.Select(attrs={'class': 'form-select'}),
            'dosage_form': forms.Select(attrs={'class': 'form-select'}),
        }


class TakerManagementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicine'].choices = [
            ("", "服用薬")] + list(self.fields['medicine'].choices)[1:]
        self.fields['medicine'].required = False

    class Meta:
        model = MedicineMangement
        fields = {'medicine'}
        widgets = {
            'medicine': forms.Select(attrs={'class': 'form-select'}),
        }
