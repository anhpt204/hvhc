# -*- encoding: utf-8 -*-

from django.contrib.admin.options import TabularInline, ModelAdmin
from tracnghiem.models import Answer, QuestionGroup_Setting, Chapter_Setting,\
    CaThi, QuestionGroup, MCQuestion, TFQuestion, SinhDeConf, LogSinhDe

from django.contrib import admin

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
    
    list_display = ('id', 'monHoc', 'doiTuong', 'noiDung', 'taoBoi', 'thuocChuong', 'prior', 'level')
    list_filter = ('monHoc', 'doiTuong')
    fields = ('monHoc', 'doiTuong', 
              'prior', 'thuocChuong', 'taoBoi',
              'noiDung', 'figure', 'audio', 'clip'  )

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
        ds_dethi = obj.sinhDe()
        return u'<a href="%s">Sinh đề</a>' % ('/hvhc/tracnghiem/sinhde/'+str(obj.pk)+'/')
    sinhDe.allow_tags=True
    sinhDe.short_description="Sinh đề"
    
class TFQuestionAdmin(ModelAdmin    ):
    model = TFQuestion
    list_display = ('monHoc', 'doiTuong', 'noiDung', 'taoBoi')
    fields = ('monHoc', 'doiTuong', 'prior', 'thuocChuong', 'taoBoi',
              'noiDung', 'figure', 'audio', 'clip', 'isTrue' )
    list_filter = ('monHoc',)
    
    
# class EssayQuestionAdmin(ModelAdmin):
#     list_display=('mon_thi', 'content',)
#     list_filter = ('mon_thi',)
#     fields = ('mon_thi', 'content',
#               'figure', 'question_group', 'answer' )
    
admin.site.register(LogSinhDe, LogSinhDeAdmin)
# admin.site.register(CaThi, CaThiAdmin)
admin.site.register(QuestionGroup, QuestionGroupAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(TFQuestion, TFQuestionAdmin)
