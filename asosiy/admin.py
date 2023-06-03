from django.contrib import admin
from .models import *

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_filter = ('ish_vaqt',)
    search_fields = ('ism',)


@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ("id","ism","kurs","kitob_soni")
    list_display_links = ("ism",)
    list_editable = ("kurs","kitob_soni")
    list_filter = ("kurs",)
    search_fields = ("ism", "id", "kurs")
    list_per_page = 5

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ("nom","janr","sahifa")
    list_display_links = ("nom",)
    list_editable = ("sahifa",)
    search_fields = ("nom","muallif__ism")
    list_filter = ("janr",)
    autocomplete_fields = ("muallif",)

@admin.register(Mualllif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('ism','id','tirik','kitob_soni')
    search_fields = ("ism",)
    list_display_links = ('id','ism')
    list_filter = ('tirik',)
    list_editable = ('kitob_soni','tirik')

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('talaba','kitob','admin')
    autocomplete_fields = ('talaba','kitob','admin')
    list_display_links = ('talaba',)



# admin.site.register(Talaba)
# admin.site.register(Kitob)
# admin.site.register(Admin)
# admin.site.register(Record)



