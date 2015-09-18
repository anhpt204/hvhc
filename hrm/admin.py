# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.contrib.admin.options import TabularInline, ModelAdmin
from hrm.models import SinhVien, DonVi, GiaoVien
from django.contrib import admin

class SinhVienInLine(TabularInline):
    model = SinhVien;
#     fields = ('ma_sv', 'ho_ten', 'gioi_tinh', 'ngay_sinh', 'que_quan')
    fields = ('ma_sv', 'ho_ten')
    
class DonViAdmin(ModelAdmin):
    model = DonVi
    
class GiaoVienAdmin(ModelAdmin):
    model = GiaoVien
    fields = ('ma_so', 'ho_ten', 'don_vi')
    list_display=('ma_so','ho_ten','don_vi')
    search_fields=('ho_ten',)
    list_filter = ('don_vi',)
    
class SinhVienAdmin(ModelAdmin):
    model = SinhVien
    
    fields = ('ma_sv', 'ho_ten', 'lop')
    list_display = ('ma_sv', 'ho_ten', 'lop')
    search_fields = ('ho_ten',)
    list_filter = ('lop',)

admin.site.register(DonVi, DonViAdmin)
admin.site.register(GiaoVien, GiaoVienAdmin)
admin.site.register(SinhVien, SinhVienAdmin)