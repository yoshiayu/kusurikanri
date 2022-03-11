from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import signinview, loginview, topview, timesettingview, takermanegementview, settingtopview, medicineregistrationview, managementtopview, TakermanegemenDelete, MedicineRegistrationCreate, TakerManegementCreate, ManagementTopCreate, SigninCreate, TimeSettingUpdate

urlpatterns = [
    path("signin/", signinview, name="signin"),
    path("login/", loginview, name="login"),
    path("top/", topview, name="top"),
    path("timesetting/", timesettingview, name="timesetting"),
    path("takermanegement", takermanegementview, name="takermanegement"),
    path("settingtop", settingtopview, name="settingtop"),
    path("medicineregistration/", medicineregistrationview,
         name="medicineregistration"),
    path("managementtop/", managementtopview, name="managementtop"),
    path('delete/<int:pk>', TakermanegemenDelete.as_view(), name='delete'),
    path('create/<int:pk>', MedicineRegistrationCreate.as_view()),
    path('create/<int:pk>', TakerManegementCreate.as_view()),
    path('update/<int:pk>', TimeSettingUpdate.as_view(), name='update'),
    path('create/<int:pk>', ManagementTopCreate.as_view()),
    path('create/<int:pk>', SigninCreate.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
