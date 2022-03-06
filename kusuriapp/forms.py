from django import forms
from .models import TakingTimeAlarm, MedicineMangement


class TimeSettingForm(forms.ModelForm):
    class Meta:
        model = TakingTimeAlarm
        fields = '__all__'


class ManagementTopForm(forms.ModelForm):
    class Meta:
        model = MedicineMangement
        fields = '__all__'
