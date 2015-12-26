# -*- encoding: utf-8 -*-

from django.contrib.admin.options import TabularInline, ModelAdmin
from tracnghiem.models import Answer, QuestionGroup, MCQuestion, TFQuestion, SinhDeConf, LogSinhDe,\
    NganHangDe, KHThi, BaiThi

from django.contrib import admin
import json

class AnswerInLine(TabularInline):
    model = Answer
    extra=4
    max_num=4
    
# class QuestionGroup_SettingInLine(TabularInline):
#     model = QuestionGroup_Setting
#     fields=('question_group', 'question_type', 'mark_per_question', 'num_of_questions')

class SinhDeConfInline(TabularInline):
    model = SinhDeConf
    fields = ('level', 'loaiCauHoi', 'soLuong')
    
# class Chapter_SettingInLine(TabularInline):
#     model = Chapter_Setting
#     fields=('chapter', 'num_of_questions')
    
# class CaThiAdmin(ModelAdmin):
# #     form = CaThiAdminForm
#     model = CaThi
#     filter_horizontal =('ds_thisinh', 'ds_giamthi')
# #     form = CaThiForm
#     list_display = ('title', 'mon_thi', 'ngay_thi', 'description')
#     fields=('title', 'mon_thi', 'ds_giamthi', 'ds_thisinh', 'ngay_thi', 
#             'tg_bat_dau', 'tg_ket_thuc', 'pass_mark','tao_moi_de_thi',
#             'description')
# #     exclude=('ds_sv_thi',)
# 
#     def add_view(self, request, form_url='', extra_context=None):
#         self.inlines = []
#         return ModelAdmin.add_view(self, request, form_url=form_url, extra_context=extra_context)
# 
#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         self.inlines = [QuestionGroup_SettingInLine, Chapter_SettingInLine]
#         return ModelAdmin.change_view(self, request, object_id, form_url=form_url, extra_context=extra_context)
# 
class QuestionGroupAdmin(ModelAdmin):
    model = QuestionGroup
     
    
class MCQuestionAdmin(ModelAdmin):
    model=MCQuestion
    
    list_display = ('maCauHoi', 'monHoc', 'doiTuong', 'noiDung', 'taoBoi', 'thuocChuong', 'prior', 'level')
    list_filter = ('monHoc', 'doiTuong')
    fields = ('maCauHoi', 'monHoc', 'doiTuong', 
              'prior', 'thuocChuong', 'taoBoi',
              'noiDung', 'figure', )#'audio', 'clip'  )

    search_fields = ('noiDung',)
#     filter_horizontal = ('ca_thi',)
    
    inlines = [AnswerInLine]
    
    
class LogSinhDeAdmin(ModelAdmin):
    model = LogSinhDe
    fields = ("monHoc", 'doiTuong', 'soLuong', 'ngayTao')
    list_display=("monHoc", 'doiTuong', 'ngayTao', 'nguoiTao', 'soLuong', 'sinhDe')
    inlines=[SinhDeConfInline]
    
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.nguoiTao = request.user
        instance.save()
    
    def sinhDe(self, obj):
#         ds_dethi = obj.sinhDe()
        return u'<a href="%s">Sinh đề</a>' % ('/hvhc/tracnghiem/sinhde/'+str(obj.pk)+'/')
    sinhDe.allow_tags=True
    sinhDe.short_description="Sinh đề"
    
class TFQuestionAdmin(ModelAdmin):
    model = TFQuestion
    list_display = ('monHoc', 'doiTuong', 'noiDung', 'taoBoi')
    fields = ('monHoc', 'doiTuong', 'prior', 'thuocChuong', 'taoBoi',
              'noiDung', 'figure', 'audio', 'clip', 'isTrue' )
    list_filter = ('monHoc',)
    
class NganHangDeAdmin(ModelAdmin):
    model=NganHangDe
    list_display=('maDeThi', 'get_monHoc', 'get_doiTuong', 'ngay_tao', 'daDuyet', 'export_pdf')
    
    list_filter=('logSinhDe__doiTuong', 'logSinhDe__monHoc', 'ngay_tao', 'daDuyet')
    actions=['duyet_deThi', 'boDuyet_deThi']
    
    
    def get_monHoc(self, obj):
        return obj.logSinhDe.monHoc
    get_monHoc.short_description="Môn thi"

    def get_doiTuong(self, obj):
        return obj.logSinhDe.doiTuong
    get_doiTuong.short_description="Đối tượng"

    def duyet_deThi(self, request, queryset):
        queryset.update(daDuyet=True)
    duyet_deThi.short_description = "Duyệt các đề đã chọn"
    
    def boDuyet_deThi(self, request, queryset):
        queryset.update(daDuyet=False)
    boDuyet_deThi.short_description = "Bỏ duyệt các đề đã chọn"
    
    def export_pdf(self, obj):
        return u'<a href="%s">PDF</a>' % ('/hvhc/tracnghiem/export/dethi/'+str(obj.pk)+'/')
    export_pdf.allow_tags=True
    export_pdf.short_description="Đề thi"

class KHThiAdmin(ModelAdmin):    
    model=KHThi
    filter_horizontal =('ds_thisinh', 'ds_giamthi')
    list_display = ['ten', 'mon_thi', 'doi_tuong', 'nam_hoc', 'hoc_ky', 
                    'ngay_thi', 'tg_bat_dau', 'tg_ket_thuc', 'boc_tron_de']
    
    fields = ['ten', 'mon_thi', 'nam_hoc', 'hoc_ky', 'doi_tuong', 
            'ds_thisinh',
            'ds_giamthi', 
              'ngay_thi', 'tg_bat_dau', 'tg_ket_thuc']
    
    def boc_tron_de(self, obj):
        dethi = json.loads(obj.de_thi)
        if len(dethi) == 0:
            return u'<a href="%s">Bốc đề</a>' % ('/hvhc/tracnghiem/khthi/boctrondethi/'+str(obj.pk)+'/')
        else:
            return u'<a href="%s">Đã có</a>, <a href="%s">Bốc lại</a>' % ('/hvhc/tracnghiem/khthi/show/'+str(obj.pk)+'/','/hvhc/tracnghiem/khthi/boctrondethi/'+str(obj.pk)+'/')
   
    boc_tron_de.allow_tags=True
    boc_tron_de.short_description="Thực hiện"
    
class DiemAdmin(ModelAdmin):
    model = BaiThi
    list_display = ['thi_sinh', 'diem']
    
admin.site.register(LogSinhDe, LogSinhDeAdmin)
admin.site.register(NganHangDe, NganHangDeAdmin)
admin.site.register(QuestionGroup, QuestionGroupAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(TFQuestion, TFQuestionAdmin)
admin.site.register(KHThi, KHThiAdmin)
admin.site.register(BaiThi, DiemAdmin)