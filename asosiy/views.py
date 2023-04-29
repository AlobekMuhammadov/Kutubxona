from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# def salomlash(request):
#     return HttpResponse("<h1>salom, dunyo!</h1>")
# def bosh_sahifa(request):
#     return render(request,'Kutubxona.html')
# def mashq_uchun(requests):
#     content = {
#         "kitoblar":["Ufq","qorqma","Otkan kunlar", "odamiylik mulki"],
#         "ism":"Abdulhamid"
#
#     }
#     return render (requests,'mashq.html',content)
#
def talabalar(requests):
    soz = requests.GET.get("qidiruv")
    if soz == "" or soz is None:
        content = {
            "students":Talaba.objects.all()
        }
    else:
        content = {
            "students":Talaba.objects.filter(ism__icontains=soz)
        }
    return render(requests,'talabalar.html', content)
#
# def bitiruvchi(requests):
#     content = {
#         "bitiruvchi":Talaba.objects.filter(kurs=4)
#     }
#     return render(requests,'bitiruvchi.html',content)
#
#
# def kitobxon(requests):
#     content = {
#         "kitobxon":Talaba.objects.filter(kitob_soni__gt=0)
#     }
#     return render(requests,'kitobxonlar.html',content)
#
# def bitta_talaba(requets, son):
#     content = {
#         "talaba":Talaba.objects.get(id=son)
#
#     }
#     return render(requets, 'bitta_talaba.html', content)
#
# def ismi_a(requests):
#     content = {
#         "talaba":Talaba.objects.filter(ism__icontains='a')
#     }
#     return render(requests,'ism_a.html',content)
#
#
# def bitta_record(requets, son):
#     content = {
#         "record":Record.objects.get(id=son)
#
#     }
#     return render(requets, 'bitta_record.html', content)


def hamma_talaba(requests):
    content = {
        "talabalar":Talaba.objects.all()
    }
    return render(requests,'talabalar.html',content)


def bitiruvchilar(requests):
    content = {
        "bitiruvchilar":Talaba.objects.filter(kurs__gt=3)
    }
    return render(requests, 'bitiruvchilar',content)

def kitobxon(requests):
    content = {
        "kitobxon":Talaba.objects.filter(kitob_soni__gt=0)
    }
    return render(requests,'kitobxonlar.html',content)


def ismi_a(requests):
    content = {
        "talaba":Talaba.objects.filter(ism__icontains='a')
    }
    return render(requests,'ism_a.html',content)


def bitta_talaba(requets, son):
    content = {
        "talaba":Talaba.objects.get(id=son)
    }
    return render(requets, 'bitta_talaba.html', content)




def talaba_ochir(requests,son):
    Talaba.objects.filter(id=son).delete()
    return redirect('/talabalar/')


def kitoblar(requests):
    soz = requests.GET.get("qidiruv")
    if soz == "" or soz is None:
        content={
            "kitoblar":Kitob.objects.all()
        }
    else:
        content = {
            "kitoblar":Kitob.objects.filter(nom__icontains=soz)
        }
    return render(requests, 'kitoblar.html',content)


# def kitobilar(requests):
#     content = {
#         "kitoblar":Kitob.objects.all()
#     }
#     return render(requests,'kitoblar.html',content)



def kitob_ochir(requests,son):
    Kitob.objects.filter(id=son).delete()
    return redirect('/kitoblar/')


# def kitobilar(requests,son):
#     content = {
#         "kitob":Kitob.objects.get(son=id)
#     }
#     return render(requests,"kitoblar.html",content)
# ######
#     path('kitoblar/<int:son>/', kitobilar),



# def recordlar(requests):
#     content = {
#         "recordlar":Record.objects.all()
#     }
#     return render(requests,'records/html',content)
# #########
#     path ('records/', recordlar),


# def tirik_muallif(requests):
#     content = {
#         "tirik_mualliflar":Mualllif.objects.filter(tirik=True)
#     }
#     return render(requests,'muallif.html',content)
# ##############
#     path ('tirik_muallif/', tirik_muallif),


# def sahifa_top3(requests):
#     content ={
#         "sahifa_top3":Kitob.objects.all().order_by('-sahifa')[0:3]
#     }
#     return render(requests,'kitob.html',content)
# ###########
#     path ('sahifa_top3/', sahifa_top3),


# def kitob_order_top3(requests):
#     content = {
#         "kitob_top3":Mualllif.objects.all().order_by('-kitob_soni')[0:3]
#     }
#     return render(requests,"muallif.html",content)
# ##########
#     path ('kitob_order_top3/', kitob_order_top3),




















