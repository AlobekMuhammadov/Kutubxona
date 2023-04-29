from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=16)
    kitob_soni = models.SmallIntegerField(default=0)
    kurs = models.SmallIntegerField()
    def __str__(self):
        return self.ism

class Mualllif(models.Model):
    ism = models.CharField(max_length=16)
    kitob_soni = models.SmallIntegerField(null=True,blank=True)
    jins = models.CharField(max_length=50,choices=[('Ayol','Ayol'),('Erkak','Erkak')])
    tirik = models.BooleanField(choices=[(True,True),(False,False)])
    tugilgan_yil = models.SmallIntegerField()
    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=50)
    muallif = models.ForeignKey(Mualllif,on_delete=models.CASCADE)
    sahifa = models.SmallIntegerField(null=True,blank=True)
    janr = models.CharField(max_length=20)
    def __str__(self):
        return self.nom


class Admin(models.Model):
    ism = models.CharField(max_length=16)
    ish_vaqt = models.CharField(max_length=40,choices=[('08:00 | 18:00','08:00 | 18:00'),('18:00 | 08:00','18:00 | 08:00')])
    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba = models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob,on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sana = models.DateField()
    qaytgan_qaytmagan = models.BooleanField()











