from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(),name='register'),
    path('talabalar/', talabalar),
    path('talaba_tahrir/<int:son>/', talaba_tahrir),
    path('kitob_edit/<int:son>/', kitob_edit),
    path('mualliflar/', mualliflar),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('recordlar/', records),
    path('talaba/<int:son>/', bitta_talaba),
    path('record/<int:son>/', bitta_record),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('record_ochir/<int:son>/', record_ochir),
    path('kitoblar/', kitoblar),
    path('adminlar/', adminlar),
    path('admin_edit/<int:son>', admin_edit),
    path('kitob_ochir/<int:son>/', kitob_ochir),
]
