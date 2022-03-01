from django.urls import path
from .views import AppList, AppDetail, AppCreate

urlpatterns = [
    # ListView Userモデル
    path('email/', AppList.as_view()),
    path('first_name/', AppList.as_view()),
    path('last_name/', AppList.as_view()),
    path('is_staff/', AppList.as_view()),
    path('is_active/', AppList.as_view()),
    path('date_joined/', AppList.as_view()),
    path('user_id/', AppList.as_view()),
    path('login_id/', AppList.as_view()),
    path('create_data/', AppList.as_view()),
    path('update_data/', AppList.as_view()),
    path('delete_data/', AppList.as_view()),
    # ListView MedicineNameManagemenモデル
    path('user_id/', AppList.as_view()),
    path('name/', AppList.as_view()),
    # ListView MedicineMangementモデル
    path('user_id/', AppList.as_view()),
    path('name/', AppList.as_view()),
    path('medicine/', AppList.as_view()),
    path('taking_dossage/', AppList.as_view()),
    path('taking_unit/', AppList.as_view()),
    path('taking_time/', AppList.as_view()),
    path('taking_start/', AppList.as_view()),
    path('taking_end/', AppList.as_view()),
    path('text/', AppList.as_view()),
    # ListView TakingTimeAlarmモデル
    path('taking_time/', AppList.as_view()),

    # DetailView Userモデル
    path('email/', AppDetail.as_view()),
    path('first_name/', AppDetail.as_view()),
    path('last_name/', AppDetail.as_view()),
    path('is_staff/', AppDetail.as_view()),
    path('is_active/', AppDetail.as_view()),
    path('date_joined/', AppDetail.as_view()),
    path('user_id/', AppDetail.as_view()),
    path('login_id/', AppDetail.as_view()),
    path('create_data/', AppDetail.as_view()),
    path('update_data/', AppDetail.as_view()),
    path('delete_data/', AppDetail.as_view()),
    # DetailView MedicineNameManagemenモデル
    path('user_id/', AppDetail.as_view()),
    path('name/', AppDetail.as_view()),
    # DetailView MedicineMangementモデル
    path('user_id/', AppDetail.as_view()),
    path('name/', AppDetail.as_view()),
    path('medicine/', AppDetail.as_view()),
    path('taking_dossage/', AppDetail.as_view()),
    path('taking_unit/', AppDetail.as_view()),
    path('taking_time/', AppDetail.as_view()),
    path('taking_start/', AppDetail.as_view()),
    path('taking_end/', AppDetail.as_view()),
    path('text/', AppDetail.as_view()),
    # DetailView TakingTimeAlarmモデル
    path('taking_time/', AppDetail.as_view()),

    # CreatelView Userモデル
    path('email/', AppCreate.as_view()),
    path('first_name/', AppCreate.as_view()),
    path('last_name/', AppCreate.as_view()),
    path('is_staff/', AppCreate.as_view()),
    path('is_active/', AppCreate.as_view()),
    path('date_joined/', AppCreate.as_view()),
    path('user_id/', AppCreate.as_view()),
    path('login_id/', AppCreate.as_view()),
    path('create_data/', AppCreate.as_view()),
    path('update_data/', AppCreate.as_view()),
    path('delete_data/', AppCreate.as_view()),
    # CreateView MedicineNameManagemenモデル
    path('user_id/', AppCreate.as_view()),
    path('name/', AppCreate.as_view()),
    # CreateView MedicineMangementモデル
    path('user_id/', AppCreate.as_view()),
    path('name/', AppCreate.as_view()),
    path('medicine/', AppCreate.as_view()),
    path('taking_dossage/', AppCreate.as_view()),
    path('taking_unit/', AppCreate.as_view()),
    path('taking_time/', AppCreate.as_view()),
    path('taking_start/', AppCreate.as_view()),
    path('taking_end/', AppCreate.as_view()),
    path('text/', AppCreate.as_view()),
    # CreateView TakingTimeAlarmモデル
    path('taking_time/', AppCreate.as_view()),
]
