from django.urls import path
from kusuriapp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('excel_export/', views.IndexView.excel_export, name='excel_export'),
]