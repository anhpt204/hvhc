# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.contrib.admin.options import TabularInline, ModelAdmin
from tuluan.models import DeThi, BoDe, CaThi
from os.path import basename
from django.contrib import admin

class DeThiInline(TabularInline):
    model = DeThi
    
class DeThiAdmin(ModelAdmin):
    model = DeThi
    
    list_display =['ma_de_thi', 'get_doi_tuong', 'get_mon_thi', 'get_de_thi','get_dap_an']
    
    list_filter =('ngan_hang__doi_tuong', 'ngan_hang__mon_thi',)
    search_fields = ['ma_de_thi',]
    
    def get_doi_tuong(self, obj):
        if obj.ngan_hang:
            return obj.ngan_hang.doi_tuong.ten_dt
    get_doi_tuong.allow_tags=True
    get_doi_tuong.short_description="Đối tượng"

    def get_mon_thi(self, obj):
        if obj.ngan_hang:
            return obj.ngan_hang.mon_thi
    get_mon_thi.allow_tags=True
    get_mon_thi.short_description="Môn thi"
        
    def get_de_thi(self, obj):
        if obj.de_thi:
            return u'<a href="%s">%s</a>' % ('/quiz/tuluan/preview/dethi/'+str(obj.pk)+'/', basename(obj.de_thi.path))
        else:
            return u'(Chưa có)'
    get_de_thi.allow_tags=True
    get_de_thi.short_description="Đề thi"

    def get_dap_an(self, obj):
        if obj.dap_an:
            return u'<a href="%s">%s</a>' % ('/quiz/tuluan/preview/dapan/'+str(obj.pk)+'/', basename(obj.dap_an.path))
        else:
            return u'(Chưa có)'
    get_dap_an.allow_tags=True
    get_dap_an.short_description="Đáp án"
        
    def view_pdf(self,obj):
        if obj.de_thi:            
            return u'<a href="%s">View</a>' % ('/quiz/tuluan/preview/'+str(obj.pk)+'/')
        else:
            return '(no file found)'
        
    view_pdf.allow_tags = True
    view_pdf.short_description = 'Xem'
    
class BoDeAdmin(ModelAdmin):
    model = BoDe
    inlines=[DeThiInline]
    list_display = ['ma_so', 'doi_tuong', 'mon_thi', 'ngay_tao']
    

class CaThiAdmin(ModelAdmin):
    model=CaThi
    filter_horizontal =('giam_thi',)
    
    fields=('ten_ca_thi', 'nam_hoc', 'hoc_ky', 'doi_tuong', 'mon_thi', 'lop', 'ngay_thi', 'giam_thi', 'so_de_thi')
    list_display=('ten_ca_thi', 'nam_hoc', 'hoc_ky', 'doi_tuong', 'mon_thi', 'lop', 'ngay_thi', 'so_de_thi', 'get_de_thi')
    
    def get_de_thi(self, obj):
        if obj.ds_de_thi    :            
            return u'<a href="%s">Tạo đề</a>' % ('/quiz/tuluan/get_dt/'+str(obj.pk)+'/')
        else:
            return '(no file found)'
        
    get_de_thi.allow_tags = True
    get_de_thi.short_description = 'Đề thi'
    

admin.site.register(BoDe, BoDeAdmin)
admin.site.register(DeThi, DeThiAdmin)
admin.site.register(CaThi, CaThiAdmin)