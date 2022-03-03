from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import signinview, topview, timesettingview, takermanegementview, settingtopview, medicineregistrationview, managementtopview

urlpatterns = [
    path("signin", signinview, name="signin"),
    path("top", topview, name="top"),
    path("timesetting", timesettingview, name="timesetting"),
    path("takermanegement", takermanegementview, name="takermanegement"),
    path("settingtop", settingtopview, name="settingtop"),
    path("medicineregistration", medicineregistrationview,
         name="medicineregistration"),
    path("managementtop", managementtopview, name="managementtop"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
