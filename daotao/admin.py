# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.contrib.admin.options import ModelAdmin, TabularInline
from daotao.models import Lop, DoiTuong, MonThi, SinhVien, ImportSinhVien
from django.contrib import admin

class SinhVienInLine(TabularInline):
    model = SinhVien;
#     fields = ('ma_sv', 'ho_ten', 'gioi_tinh', 'ngay_sinh', 'que_quan')
    fields = ('ma_sv', 'ho_dem', 'ten')

class LopAdmin(ModelAdmin):
    model=Lop
    
    inlines = [SinhVienInLine]
    
class DoiTuongAdmin(ModelAdmin):
    model = DoiTuong
    
class MonThiAdmin(ModelAdmin):
    model=MonThi
    
class SinhVienAdmin(ModelAdmin):
    model = SinhVien
    
    fields = ('ma_sv', 'ho_dem', 'ten', 'lop')
    list_display = ('ma_sv', 'get_ho_ten', 'lop')
    search_fields = ('ten',)
    list_filter = ('lop',)
    
class ImportSinhVienAdmin(ModelAdmin):
    model = ImportSinhVien
    list_display=['lop', 'import_file', 'import_data']
    
    def import_data(self, obj):
#         obj.import_data()
        return u'<a href="%s">Import</a>' % ('/hvhc/daotao/import/sinhvien/'+str(obj.pk)+'/')
   
    import_data.allow_tags=True
    import_data.short_description="Import"    
    
    
admin.site.register(Lop, LopAdmin)
admin.site.register(DoiTuong, DoiTuongAdmin)
admin.site.register(MonThi, MonThiAdmin)
admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(ImportSinhVien, ImportSinhVienAdmin)
