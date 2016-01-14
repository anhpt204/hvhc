# -*- encoding: utf-8 -*-

from django.contrib.admin.options import TabularInline, ModelAdmin
from tracnghiem.models import Answer, QuestionGroup, MCQuestion, TFQuestion, SinhDeConf, LogSinhDe,\
    NganHangDe, KHThi, BaiThi, ImportMCQuestion, ImportSinhVien

from django.contrib import admin
import json
# from django.contrib.auth.decorators import permission_required
from permission.decorators import permission_required
from hvhc import PERM_BOC_DE, PERM_XEM_IN_DE
from daotao.models import SinhVien

#Override modeladmin
class MyModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if hasattr(self, 'field_permissions'):
            user = request.user
            for _field in self.opts.fields:
                perm = self.field_permissions.get(_field.name)
                if perm and not user.has_perm(perm):
                    if self.exclude:
                        self.exclude.append(_field.name)
                    else:
                        self.exclude=[_field.name]
        return super(MyModelAdmin, self).get_form(request, obj, **kwargs)
    

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
    
    list_display = ('maCauHoi', 'monHoc', 'doiTuong', 'noiDung', 'taoBoi', 'thuocChuong', 'prior', 'diem')
    list_filter = ('monHoc', 'doiTuong')
    fields = ('maCauHoi', 'monHoc', 'doiTuong', 
              'prior', 'thuocChuong', 'taoBoi',
              'noiDung', 'diem', 'figure', )#'audio', 'clip'  )

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
    
    fields = ['ten', 'mon_thi', 'nam_hoc', 'hoc_ky', 'doi_tuong', 
            'ds_thisinh',
            'ds_giamthi', 
              'ngay_thi', 'tg_bat_dau', 'tg_thi', 'trang_thai']
    
#     field_permissions = {'boc_tron_de':'tracnghiem.khthi.duoc_phep_boc_de',
# #                          'in_de':'khthi.duoc_phep_xem_va_in_de'
#                         }
    
#     @permission_required('tracnghiem.khthi.duoc_phep_boc-de')
    def boc_tron_de(self, obj):
        dethi = json.loads(obj.de_thi)
        
        if len(dethi) == 0:
            return u'<a href="%s">Bốc đề</a>' % ('/hvhc/tracnghiem/khthi/boctrondethi/'+str(obj.pk)+'/')
        else:
            return u'Đã có, <a href="%s">Bốc lại</a>' % ('/hvhc/tracnghiem/khthi/boctrondethi/'+str(obj.pk)+'/')
   
    boc_tron_de.allow_tags=True
    boc_tron_de.short_description="Thực hiện"
    
    def xem_de(self, obj):
        dethi = json.loads(obj.de_thi)
        
        if len(dethi) == 0:
            return u'Chưa có'
        else:
            return u'<a href="%s">Xem đề</a>' % ('/hvhc/tracnghiem/khthi/show/'+str(obj.pk)+'/')
   
    xem_de.allow_tags=True
    xem_de.short_description="Xem"
    
    
    def get_list_display(self, request):
        ld = ['ten', 'mon_thi', 'doi_tuong', 'nam_hoc', 'hoc_ky', 
                    'ngay_thi', 
                    'tg_bat_dau', 'tg_thi', 'trang_thai', 'nguoi_boc_de']

        allow_boc_de = False
        allow_xem_de = False
        
        perms = request.user.user_permissions.all()
        for perm in perms:
            if PERM_BOC_DE == perm.codename:
                allow_boc_de = True
                break
            
            if perm.codename == PERM_XEM_IN_DE:
                allow_xem_de = True
                break
            
        for group in request.user.groups.all():
            perms = group.permissions.all()
            for perm in perms:
                if PERM_BOC_DE == perm.codename:
                    allow_boc_de = True
                    break
            
                if perm.codename == PERM_XEM_IN_DE:
                    allow_xem_de = True
                    break
        if allow_boc_de:
            ld.append('boc_tron_de')
        if allow_xem_de:
            ld.append('xem_de')        
        return ld

#         return ModelAdmin.get_list_display(self, request)
class DiemAdmin(ModelAdmin):
    model = BaiThi
    list_display = ['get_ma_sv', 'get_ho_ten', 'get_lop', 'get_mon_thi', 'diem']
    
    def get_ma_sv(self, obj):
        return obj.thi_sinh.ma_sv
    get_ma_sv.short_description = 'Mã SV'

    def get_ho_ten(self, obj):
        return obj.thi_sinh.ho_ten
    get_ho_ten.short_description = 'Họ và tên'

    def get_lop(self, obj):
        return obj.thi_sinh.lop
    get_lop.short_description = 'Lớp'

    def get_mon_thi(self, obj):
        return obj.khthi.mon_thi
    get_mon_thi.short_description='Môn thi'
        
class ImportMCQuestionAdmin(ModelAdmin):
    model = ImportMCQuestion
    list_display=['mon_thi', 'doi_tuong', 'khoa', 'import_file', 'import_data']
    
    def import_data(self, obj):
#         obj.import_data()
        return u'<a href="%s">Import</a>' % ('/hvhc/tracnghiem/import/mc/'+str(obj.pk)+'/')
   
    import_data.allow_tags=True
    import_data.short_description="Import"
    
class ImportSinhVienAdmin(ModelAdmin):
    model = ImportSinhVien
    list_display=['lop', 'import_file']
    
admin.site.register(LogSinhDe, LogSinhDeAdmin)
admin.site.register(NganHangDe, NganHangDeAdmin)
admin.site.register(QuestionGroup, QuestionGroupAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(TFQuestion, TFQuestionAdmin)
admin.site.register(KHThi, KHThiAdmin)
admin.site.register(BaiThi, DiemAdmin)
admin.site.register(ImportMCQuestion, ImportMCQuestionAdmin)
admin.site.register(ImportSinhVien, ImportSinhVienAdmin)
