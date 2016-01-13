# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.contrib.admin.options import TabularInline, ModelAdmin
from hrm.models import DonVi, GiaoVien
from django.contrib import admin

    
class DonViAdmin(ModelAdmin):
    model = DonVi
    
class GiaoVienAdmin(ModelAdmin):
    model = GiaoVien
    fields = ('ma_so', 'ho_ten', 'don_vi')
    list_display=('ma_so','ho_ten','don_vi')
    search_fields=('ho_ten',)
    list_filter = ('don_vi',)
    


admin.site.register(DonVi, DonViAdmin)
admin.site.register(GiaoVien, GiaoVienAdmin)
