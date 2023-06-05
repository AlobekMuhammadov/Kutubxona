from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import *


def adminlar(request):
    if request.method == 'POST':
        f = AdminForms(request.POST)
        if f.is_valid():
            Admin.objects.create(
                ism=f.cleaned_data['ism'],
                ish_vaqti=f.cleaned_data.get('i_v')
            )
        return redirect('/adminlar/')
    content={
        "adminlar":Admin.objects.all(),
        "forma": AdminForms()
    }
    return render(request,'admins.html',content)


def talabalar(request):
    if request.method == 'POST':
        f = TalabaForm(request.POST)
        if f.is_valid():
            Talaba.objects.create(
                ism = f.cleaned_data.get('ism'),
                kurs = f.cleaned_data.get('kursi'),
                kitob_soni = f.cleaned_data.get('k_s')
        )
        return redirect('/talabalar/')


    soz = request.GET.get("qidiruv")
    if soz == "" or soz is None:
        content = {
            "students":Talaba.objects.all(),
            'forma':TalabaForm()
        }
    else:
        content = {
            "students":Talaba.objects.filter(ism__icontains=soz),
            'forma': TalabaForm()
        }
    return render(request,'talabalar.html', content)





def bitta_talaba(requets, son):
    content = {
        "talaba":Talaba.objects.get(id=son)

    }
    return render(requets, 'bitta_talaba.html', content)



def bitta_record(requets, son):
    content = {
        "record":Record.objects.get(id=son)

    }
    return render(requets, 'bitta_record.html', content)





def talaba_ochir(requests,son):
    Talaba.objects.filter(id=son).delete()
    return redirect('/talabalar/')






def mualliflar(request):
    if request.method == 'POST':
        f = MuallifForm(request.POST)
        if f.is_valid:
            Mualllif.objects.create(
                ism = f.cleaned_data.get('ism'),
                kitob_soni = f.cleaned_data.get('kitob_soni'),
                jins = f.cleaned_data.get('jins'),
                tirik=f.cleaned_data.get('tirik'),
                tugilgan_yil = f.cleaned_data.get('tugilgan_yil'),
            )
        return redirect('/mualliflar/')
    soz = request.GET.get('qidiruv')
    if soz =='' or soz is None:
        content = {
            "mualliflar":Mualllif.objects.all(),
            'forma':MuallifForm
    }

    else:
        content = {
            "mualliflar": Mualllif.objects.filter(ism__contains=soz),
            'forma':MuallifForm
        }

    return render(request,"muallif.html",content)

def muallif_ochir(request,son):
    Mualllif.objects.filter(id=son).delete()
    return redirect('/mualliflar/')




def muallif_id(requests,son):
    content = {
        "muallif":Mualllif.objects.filter(son=id)
    }
    return render(requests,'muallif.html',content)
#
    path('muallif/<int:son>/', muallif_id),





def kitob_ochir(requests,son):
    Kitob.objects.filter(id=son).delete()
    return redirect('/kitoblar/')



def record_ochir(request, son):
    Record.objects.filter(id=son).delete()
    return redirect('/recordlar/')



def kitoblar(request):
    soz = request.GET.get("qidiruv")
    if request.method == 'POST':
        f = KitobForm(request.POST)
        if f.is_valid():
            f.save()
        # Kitob.objects.create(
        #     nom = request.POST.get('nom'),
        #     janr = request.POST.get('janr'),
        #     sahifa = request.POST.get('sahifa'),
        #     muallif = Mualllif.objects.get(id=request.POST.get('m'))
        # )
        return redirect('/kitoblar')

    if soz == "" or soz is None:
        content={
            "kitoblar":Kitob.objects.all(),
            "Mualliflar": Mualllif.objects.all(),
            "forms":KitobForm()
        }
    else:
        content = {
            "kitoblar":Kitob.objects.filter(nom__icontains=soz),
            "Mualliflar":Mualllif.objects.all(),
            "forms":KitobForm()
        }
    return render(request, 'kitoblar.html',content)


def talaba_tahrir(request,son):
    if request.method == 'POST':
        Talaba.objects.filter(id=son).update(
            kurs=request.POST.get('kurs'),
            kitob_soni=request.POST.get('kitob_soni'))
        return redirect('/talabalar/')

    content = {
        "talaba":Talaba.objects.get(id=son)
    }
    return render(request,'talaba_tahrir.html', content)


def kitob_edit(request,son):
    if request.method == 'POST':
        Kitob.objects.filter(id=son).update(
            nom=request.POST.get('nom'),
            sahifa=request.POST.get('sahifa'),
            janr=request.POST.get('janr'),
            muallif=Mualllif.objects.get(id=request.POST.get('janr')))
        return redirect('/kitoblar/')
    k = Kitob.objects.get(id=son)
    content = {
        "kitoblar":k,
        "mualliflar":Mualllif.objects.exclude(id=k.muallif.id)
    }
    return render(request,'kitob_edit.html', content)


def admin_edit(request,son):
    if request.method == 'POST':
        Admin.objects.filter(id=son).update(
            ism=request.POST.get('ism'),
            kitob_soni=request.POST.get('kitob_soni'))
        return redirect('/talabalar/')

    content = {
        "talaba":Talaba.objects.get(id=son)
    }
    return render(request,'talaba_tahrir.html', content)





def records(request):
    if request.user.authenticated:
        if request.method == 'POST':
            forma = RecordForms(request.POST)
            if forma.is_valid():
                forma.save()
            return redirect('/recordlar/')
        ism = request.GET.get('qidiruv')
        if ism == "" or ism is None:
            content = {
                "record": Record.objects.all(),
                "talabalar": Talaba.objects.all(),
                "kitoblar": Kitob.objects.all(),
                "adminlar": Admin.objects.all(),
                "forma" :RecordForms()
            }
        else:
            content = {
                "record": Record.objects.filter(talaba__ism__icontains=ism),
                "talabalar": Talaba.objects.all(),
                "kitoblar": Kitob.objects.all(),
                "adminlar": Admin.objects.all(),
                "forma": RecordForms()
            }

        return render(request,'records.html',content)
    return redirect('login')

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        user = authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
        )
        if user is None:
            return redirect('login')
        login(request,user)
        return redirect('/mualliflar/')

















