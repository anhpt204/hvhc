# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.contrib.admin.options import TabularInline, ModelAdmin
from tuluan.models import DeThi, BoDe, KHThiTuLuan
from os.path import basename
from django.contrib import admin
from copy import deepcopy

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
            return u'<a href="%s">%s</a>' % ('/hvhc/tuluan/preview/dethi/'+str(obj.pk)+'/', basename(obj.de_thi.path))
        else:
            return u'(Chưa có)'
    get_de_thi.allow_tags=True
    get_de_thi.short_description="Đề thi"

    def get_dap_an(self, obj):
        if obj.dap_an:
            return u'<a href="%s">%s</a>' % ('/hvhc/tuluan/preview/dapan/'+str(obj.pk)+'/', basename(obj.dap_an.path))
        else:
            return u'(Chưa có)'
    get_dap_an.allow_tags=True
    get_dap_an.short_description="Đáp án"

    def view_pdf(self,obj):
        if obj.de_thi:
            return u'<a href="%s">View</a>' % ('/hvhc/tuluan/preview/'+str(obj.pk)+'/')
        else:
            return '(no file found)'

    view_pdf.allow_tags = True
    view_pdf.short_description = 'Xem'



class BoDeAdmin(ModelAdmin):
    model = BoDe
    inlines=[DeThiInline]
    fields=('doi_tuong', 'mon_thi', 'ngay_tao')
    list_display = ['ma_so', 'doi_tuong', 'mon_thi', 'ngay_tao']
    actions=['create_new_from_old']
    save_as = True

    def create_new_from_old(self, request, queryset):
        for obj in queryset:
            new_obj = deepcopy(obj)
            new_obj.id=None

            new_obj.save()

    create_new_from_old.short_description="Tạo bộ đề mới từ bộ đề đã có"


class KHThiTuLuanAdmin(ModelAdmin):
    model=KHThiTuLuan
    filter_horizontal =('ds_giamthi', 'ds_thisinh')

    fields=('ten', 'nam_hoc', 'hoc_ky', 'doi_tuong', 'mon_thi', 'ds_thisinh', 'ngay_thi', 'ds_giamthi', 'so_de_thi')
    list_display=('ten', 'nam_hoc', 'hoc_ky', 'doi_tuong', 'mon_thi', 'ngay_thi', 'so_de_thi', 'get_de_thi')

    def get_de_thi(self, obj):
        if obj.ds_de_thi    :
            return u'<a href="%s">Tạo đề</a>' % ('/hvhc/tuluan/get_dt/'+str(obj.pk)+'/')
        else:
            return '(no file found)'

    get_de_thi.allow_tags = True
    get_de_thi.short_description = 'Đề thi'


admin.site.register(BoDe, BoDeAdmin)
admin.site.register(DeThi, DeThiAdmin)
admin.site.register(KHThiTuLuan, KHThiTuLuanAdmin)
