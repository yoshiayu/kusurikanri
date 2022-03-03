from django.shortcuts import render


def signinview(request):
    print(request.POST.get('email_data'))
    return render(request, 'signin.html', {'somedata': 100})


def topview(request):
    print(request.POST.get(''))
    return render(request, 'top.html', {'somedata': 100})


def timesettingview(request):
    print(request.POST.get(''))
    return render(request, 'time_setting.html', {'somedata': 100})


def takermanegementview(request):
    print(request.POST.get(''))
    return render(request, 'taker_manegement.html', {'somedata': 100})


def settingtopview(request):
    print(request.POST.get(''))
    return render(request, 'setting_top.html', {'somedata': 100})


def medicineregistrationview(request):
    print(request.POST.get(''))
    return render(request, 'medicine_registration.html', {'somedata': 100})


def managementtopview(request):
    print(request.POST.get(''))
    return render(request, 'management_top.html', {'somedata': 100})
