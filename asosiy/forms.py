from .models import *
from django import forms

class TalabaForm(forms.Form):
    # def validator_ism(qiymat):
    #     if 'jon' not in qiymat or 'bek' not in qiymat or'xon' not in qiymat:
    #         raise Exception("ism mos kelmayapti")
    #     return qiymat

    def validator_ism(qiymat):
        if len(qiymat) < 3:
            raise Exception("Bunday ism kiritish mumkin emas")
        return qiymat

    ism = forms.CharField(validators=[validator_ism])
    kursi = forms.IntegerField(min_value=1, max_value=4)
    k_s = forms.IntegerField(label='Kitob soni:')



class MuallifForm(forms.Form):
    ism = forms.CharField()
    kitob_soni = forms.IntegerField()
    jins = forms.CharField()
    tirik = forms.BooleanField()
    tugilgan_yil = forms.IntegerField()



class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'


class RecordForms(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"

class AdminForms(forms.Form):
    ism = forms.CharField(max_length=30)
    i_v = forms.CharField(max_length=35)












