from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import User, MedicineMangement, MedicineNameManagement, TakingTimeAlarm


class AppList(ListView):
    template_name = 'signin.html'
    models = User


class AppList(ListView):
    template_name = 'management_top.html'
    models = MedicineMangement


class AppList(ListView):
    template_name = 'medicine_registration.html'
    models = MedicineNameManagement


class AppList(ListView):
    template_name = 'time_setting.html'
    models = TakingTimeAlarm


class AppDetail(DetailView):
    template_name = 'signin.html'
    models = User


class AppDetail(DetailView):
    template_name = 'management_top.html'
    models = MedicineMangement


class AppDetail(DetailView):
    template_name = 'medicine_registration.html'
    models = MedicineNameManagement


class AppDetail(DetailView):
    template_name = 'time_setting.html'
    models = TakingTimeAlarm


class AppCreate(CreateView):
    template_name = 'signin.html'
    models = User


class AppCreate(CreateView):
    template_name = 'management_top.html'
    models = MedicineMangement


class AppCreate(CreateView):
    template_name = 'medicine_registration.html'
    models = MedicineNameManagement


class AppCreate(CreateView):
    template_name = 'time_setting.html'
    models = TakingTimeAlarm
# Create your views here.
