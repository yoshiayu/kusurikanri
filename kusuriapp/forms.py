from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput, TimePickerInput
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
        widgets = {
            'taking_start': DateTimePickerInput(options={
                'format': 'YYYY/MM/DD HH:mm:ss',
                'locale': 'ja',
            })
        }


class CompanyMedicineNameForm(forms.ModelForm):
    class Meta:
        model = CompanyMedicineName
        fields = ['medicine_name', 'company_name', 'initials']
        lavels = {'medicine_name': '薬名',
                  'company_name': '会社名', 'initials': '頭文字'}

class ItemForm(forms.ModelForm):
    class Meta:
        # model = Item
        fields = ('sample_1', 'sample_2', 'sample_3',
                  'sample_4_start', 'sample_4_end')
        widgets = {
            'sample_1': DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),

            'sample_2': DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),

            'sample_3': TimePickerInput(
                format='%H:%M:%S',
                options={
                    'locale': 'ja',
                }

            ),

            'sample_4_start': DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).start_of('期間'),

            'sample_4_end': DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).end_of('期間'),
        }
