from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('salom/', salomlash),
    # path('mashq/', mashq_uchun),
    path('talabalar/', talabalar),
    # path('bitiruvchi/', bitiruvchi),
    # path('kitobxon/', kitobxon),
    # path('talaba/<int:son>/', bitta_talaba),
    # path('record/<int:son>/', bitta_record),
    # path('ism_a/', ismi_a),
    # path('', bosh_sahifa),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('kitoblar/', kitoblar),
    path('kitob_ochir/<int:son>/', kitob_ochir),
]
