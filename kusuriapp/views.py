from django.shortcuts import render
from django.contrib import messages
from .models import TakingTimeAlarm, CompanyMedicineName, MedicineMangement, TakingDosage, User
from .forms import TimeSettingForm, ManagementTopForm, CompanyMedicineNameForm
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy


class TakermanegemenDelete(DeleteView):
    template_name = 'taker_manegement.html'
    model = TakingDosage
    success_url = reverse_lazy('list')


class TopUpdate(UpdateView):
    template_name = 'top.html'
    model = User
    fields = ('email')
    success_url = reverse_lazy('list')


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
            TakingTimeAlarm.objects.create(
                taking_time=request.POST['taking_time'])
            messages.success(request, '時間は登録されました。')
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
    object_list = CompanyMedicineName.objects.filter(
        initials__isnull=False).order_by('initials')

    return render(request, 'medicine_registration.html', {'object_list': object_list})


def managementtopview(request):
    object_list = MedicineMangement.objects.all()
    if request.method == 'POST':
        form = ManagementTopForm(request.POST)
        if form.is_valid():
            MedicineMangement.objects.create(
                taking_start=request.POST['taking_start'],
                taking_dossage=request.POST['taking_dossage'],
                name=request.POST['name'],
                taking_unit=request.POST['taking_unit'],
                taking_end=request.POST['taking_end'],
                text=request.POST['text']
            )
            messages.success(request, '登録されました。')
    return render(request, 'management_top.html', {'object_list': object_list})
