from django.shortcuts import render
from django.contrib import messages
from .models import TakingTimeAlarm, CompanyMedicineName
from .forms import TimeSettingForm

def signinview(request):
    print(request.POST.get('email_data'))
    return render(request, 'signin.html', {'somedata': 100})


def topview(request):
    return render(request, 'top.html')


def timesettingview(request):
    object_list = TakingTimeAlarm.objects.all()
    errors = []
    if request.method == 'POST':
        form = TimeSettingForm(request.POST)
        if form.is_valid():
            TakingTimeAlarm.objects.create(taking_time=request.POST['taking_time'])
            messages.success(request, '服用時間を登録しました。')
        else:
            errors = form.errors
    return render(request, 'time_setting.html', {'object_list': object_list, 'errors': errors})


def takermanegementview(request):
    print(request.POST.get(''))
    return render(request, 'taker_manegement.html', {'somedata': 100})


def settingtopview(request):
    print(request.POST.get(''))
    return render(request, 'setting_top.html', {'somedata': 100})


def medicineregistrationview(request):
    object_list = CompanyMedicineName.objects.all()
    return render(request, 'medicine_registration.html', {'object_list': object_list})


def managementtopview(request):
    print(request.POST.get(''))
    return render(request, 'management_top.html', {'somedata': 100})
