from django import forms
from .models import TakingTimeAlarm

class TimeSettingForm(forms.ModelForm):
    class Meta:
        model = TakingTimeAlarm
        fields = '__all__'
