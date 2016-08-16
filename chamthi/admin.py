# -*- encoding: utf-8 -*-

from django.contrib import admin
from common.models import MyModelAdmin
from chamthi.models import NhapDiem, ChamDiemSV
from chamthi import *
from diem.models import TyLeDiem

from django import forms

class NhapDiemForm(forms.ModelForm):
    class Meta:
        model = NhapDiem
        fields=['diem_can_nhap']

    def __init__(self, *args, **kwargs):
        super(NhapDiemForm, self).__init__(*args, **kwargs)
        self.fields['diem_can_nhap'].queryset = TyLeDiem.objects.filter(doi_tuong=self.instance.khthi.doi_tuong)


class NhapDiemAdmin(MyModelAdmin):
    model = NhapDiem

    ld = ['khthi', 'get_mon_thi', 'get_doi_tuong', 'get_hoc_ky', 'get_ngay_thi', 'diem_can_cham', 'nhap_diem']


    # list_display = ('khthi', 'get_mon_thi', 'get_doi_tuong', 'get_hoc_ky', 'get_ngay_thi', 'trang_thai')
    list_display = ld
    form = NhapDiemForm

    def get_mon_thi(self, obj):
        return obj.khthi.mon_thi
    get_mon_thi.short_description = 'Môn thi'

    def get_doi_tuong(self, obj):
        return obj.khthi.doi_tuong
    get_doi_tuong.short_description = 'Đối tượng'

    def get_hoc_ky(self, obj):
        return obj.khthi.hoc_ky
    get_hoc_ky.short_description = 'Học kỳ'

    def get_ngay_thi(self, obj):
        return obj.khthi.ngay_thi
    get_ngay_thi.short_description = 'Ngày thi'


    def nhap_diem(self, obj):
        if obj.trang_thai == TT_CHAMTHI_CHUACODIEM:
            return u'<a href="%s">Chấm thi 1</a>' % ('/hvhc/chamthi/nhapdiem/1/'+str(obj.pk)+'/')
        elif obj.trang_thai == TT_CHAMTHI_CHAMDIEM1:
            return u'<a href="%s">Chấm thi 2</a>' % ('/hvhc/chamthi/nhapdiem/2/'+str(obj.pk)+'/')
        elif obj.trang_thai == TT_CHAMTHI_CHAMDIEM2:
            return u'<a href="%s">Dọc đường</a>' % ('/hvhc/chamthi/nhapdiem/0/'+str(obj.pk)+'/')

    nhap_diem.allow_tags=True
    nhap_diem.short_description="Nhập điểm"

    def nhap_diem_doc_duong(self, obj):
        return u'<a href="%s">Dọc đường</a>' % ('/hvhc/chamthi/nhapdiem/0/'+str(obj.pk)+'/')

    nhap_diem_doc_duong.allow_tags=True
    nhap_diem_doc_duong.short_description="Nhập điểm"

    def nhap_diem_1(self, obj):
        return u'<a href="%s">Chấm thi 1</a>' % ('/hvhc/chamthi/nhapdiem/1/'+str(obj.pk)+'/')

    nhap_diem_1.allow_tags=True
    nhap_diem_1.short_description="Nhập điểm"

    def nhap_diem_2(self, obj):
        return u'<a href="%s">Chấm thi 2</a>' % ('/hvhc/chamthi/nhapdiem/2/'+str(obj.pk)+'/')

    nhap_diem_2.allow_tags=True
    nhap_diem_2.short_description="Nhập điểm"

    def nhap_diem_3(self, obj):
        return u'<a href="%s">Chấm thi 3</a>' % ('/hvhc/chamthi/nhapdiem/3/'+str(obj.pk)+'/')

    nhap_diem_3.allow_tags=True
    nhap_diem_3.short_description="Nhập điểm"



admin.site.register(NhapDiem, NhapDiemAdmin)
