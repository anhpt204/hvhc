# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.contrib.admin.options import ModelAdmin, TabularInline
from daotao.models import Lop, DoiTuong, MonThi, SinhVien
from django.contrib import admin

class SinhVienInLine(TabularInline):
    model = SinhVien;
#     fields = ('ma_sv', 'ho_ten', 'gioi_tinh', 'ngay_sinh', 'que_quan')
    fields = ('ma_sv', 'ho_ten')

class LopAdmin(ModelAdmin):
    model=Lop
    
    inlines = [SinhVienInLine]
    
class DoiTuongAdmin(ModelAdmin):
    model = DoiTuong
    
class MonThiAdmin(ModelAdmin):
    model=MonThi
    
class SinhVienAdmin(ModelAdmin):
    model = SinhVien
    
    fields = ('ma_sv', 'ho_ten', 'lop')
    list_display = ('ma_sv', 'ho_ten', 'lop')
    search_fields = ('ho_ten',)
    list_filter = ('lop',)
    
admin.site.register(Lop, LopAdmin)
admin.site.register(DoiTuong, DoiTuongAdmin)
admin.site.register(MonThi, MonThiAdmin)
admin.site.register(SinhVien, SinhVienAdmin)