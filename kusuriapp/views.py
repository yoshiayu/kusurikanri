from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TakingTimeAlarm, CompanyMedicineName, MedicineMangement, TakingDosage, MedicineRegister
from .forms import TimeSettingForm, ManagementTopForm, CompanyMedicineNameForm
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.urls import reverse_lazy
from django.db import IntegrityError
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json


class ArticleListView(ListView):
    model = CompanyMedicineName
    template_name = "static/static/medicine_registration.html"

    def post(self, request, *args, **kwargs):
        json_body = request.body.decode("utf-8")
        body = json.loads(json_body)

        text = body["text"]

        model_data = CompanyMedicineName.objects.filter(
            medicine_name__icontains=text)[:10]

        json_data = serializers.serialize(
            "json", model_data, ensure_ascii=False, indent=2)

        return JsonResponse(json_data, safe=False)


class TakermanegemenDelete(DeleteView):
    template_name = 'taker_manegement.html'
    model = TakingDosage
    success_url = reverse_lazy('list')


class MedicineRegistrationCreate(CreateView):
    template_name = 'top.html'
    model = MedicineRegister
    fields = ('medicine')
    success_url = reverse_lazy('list')


class TakerManegementCreate(CreateView):
    template_name = 'taker_manegement.html'
    model = TakingDosage
    fields = ('name')
    success_url = reverse_lazy('list')


class TimeSettingUpdate(UpdateView):
    template_name = 'time_setting.html'
    model = MedicineMangement
    fields = ('text')
    success_url = reverse_lazy('list')


class ManagementTopCreate(CreateView):
    template_name = 'management_top.html'
    model = TakingTimeAlarm
    fields = ('taking_time')
    success_url = reverse_lazy('list')


class SigninCreate(CreateView):
    template_name = 'signin.html'
    model = User
    fields = ('email_data', 'password_data')
    success_url = reverse_lazy('list')


def signinview(request):
    if request.method == 'POST':
        email_data = request.POST['email_data']
        password_data = request.POST['password_data']
        try:
            User.objects.create_user(email_data, password_data)
            return redirect('top')
        except IntegrityError:
            return render(request, 'signin.html', {'error': 'このユーザーは既に登録されています。'})
    else:
        return render(request, 'signin.html', {})


def loginview(request):
    if request.method == 'POST':
        email_data = request.POST['email_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=email_data,
                            password=password_data)
        if user is not None:
            login(request, user)
            return redirect('top')
        else:
            return render(request, 'top.html')
    return render(request, 'top.html')


@login_required
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
    form = ManagementTopForm()
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
    return render(request, 'management_top.html', {'object_list': object_list, 'form': form})
