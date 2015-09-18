# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.contrib.admin.options import ModelAdmin
from daotao.models import Lop, DoiTuong, MonThi
from hrm.admin import SinhVienInLine
from django.contrib import admin

class LopAdmin(ModelAdmin):
    model=Lop
    
    inlines = [SinhVienInLine]
    
class DoiTuongAdmin(ModelAdmin):
    model = DoiTuong
    
class MonThiAdmin(ModelAdmin):
    model=MonThi
    
admin.site.register(Lop, LopAdmin)
admin.site.register(DoiTuong, DoiTuongAdmin)
admin.site.register(MonThi, MonThiAdmin)