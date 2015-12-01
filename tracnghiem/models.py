# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.db.models.fields import CharField, TextField, DateField, TimeField,\
    CommaSeparatedIntegerField, BooleanField, PositiveIntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from hrm.models import SinhVien, GiaoVien
from random import sample
from hvhc import MCQUESTION, TFQUESTION, QUESTION_TYPES, ANSWER_ORDER_OPTIONS,\
    ESSAYQUESTION
import json
from daotao.models import Lop, MonThi, DoiTuong
import random

# @python_2_unicode_compatible
class QuestionGroup(models.Model):
    name = CharField(verbose_name="Nhóm câu hỏi", 
                     blank=False,null=False,
                     unique=True,
                     max_length=50)
    description = TextField(verbose_name = "Ghi chú", blank=True, null=True)
    
    class Meta:
        verbose_name = "Nhóm câu hỏi"
        verbose_name_plural = "Danh sách nhóm câu hỏi"

    def __unicode__(self):
        return u'%s-%s' %(self.name, self.description)

class Lop_CaThi(models.Model):
    '''
    Dinh nghia mot lop cho moi ca thi, lop_cathi co the la ket hop cua nhieu lop
    hoac mot so sinh vien. Thich hop cho viec ghep lop thi, thi lai,...
    '''
    lop = ForeignKey(Lop, 
                     verbose_name="Lớp thi")
    
#     ds_sinhvien = ChainedForeignKey(SinhVien,
#                                     chained_field='lop',
#                                     chained_model_field='lop',
#                                     show_all=True,
#                                     auto_choose=False)
    
    ds_sinhvien = ManyToManyField(SinhVien)

class CaThi(models.Model):
    '''
    Thiet lap mot ca thi, trong do co danh sach cau hoi de tu do lam
    cac de thi cho tung sinh vien
    '''
    title = CharField(verbose_name="Ca thi", max_length=200, blank=False)
    
    description=TextField(verbose_name="Ghi chú", blank=True, null=True)
    monHoc = ForeignKey(MonThi, blank=False, null=False,
                         related_name='%(class)s_monthi_cathi',
                         verbose_name="Môn thi")
#     lop_thi = ForeignKey(Lop, blank=False, null=False,
#                          verbose_name="Lớp thi")
#     ds_thisinh = ForeignKey(Lop_CaThi, blank=False, null=False, 
#                          verbose_name="Danh sách thí sinh")
    ds_giamthi = ManyToManyField(GiaoVien, related_name='%(class)s_giamthi_cathi', 
                                 verbose_name=u'Danh sách giám thị coi thi')
    
    ds_thisinh = ManyToManyField(SinhVien, blank=False, 
                                verbose_name=u"Danh sách thí sinh")
    ds_thisinh.help_text = 'Tìm kiếm theo họ tên sinh viên hoặc mã lớp.'
    
    ngay_thi = DateField(verbose_name="Ngày thi")
    tg_bat_dau=TimeField(verbose_name="Thời gian bắt đầu")
    tg_ket_thuc=TimeField(verbose_name="Thời gian kết thúc")
    
    ds_cau_hoi = CommaSeparatedIntegerField(max_length=1024, 
                                            verbose_name="Danh sach cau hoi (ids)")
#     setting = ManyToManyField(QuestionGroup_Setting, 
#                             verbose_name="Thiết lập cấu hình ca thi")
    tao_moi_de_thi = BooleanField(blank=False, null=False,
                                  verbose_name="Tạo mới đề thi cho các sinh viên",
                                  default=True)
    
    random_order = BooleanField(blank=False, null=False,
                                verbose_name="Hiển thị câu hỏi ngẫu nhiên",
                                default=True)
    answers_at_end = BooleanField(blank=False, null=False,
                                  verbose_name="Hiển thị câu trả lời khi kết thúc",
                                  default=False)
    result_at_end = BooleanField(blank=False, null=False,
                               verbose_name="Hiển thị kết quả khi kết thúc",
                               default=True)
    exam_paper = BooleanField(blank=False, null=False,
                              verbose_name="Lưu bài thi",
                              default=True)
    single_attempt = BooleanField(blank=False, null=False,
                                  verbose_name="Mỗi người một đề thi",
                                  default=True)
    pass_mark = PositiveIntegerField(verbose_name="Điểm đạt yêu cầu")
    success_text = TextField(blank=True,
                             verbose_name="Thông báo được hiển thị nếu thí sinh vượt qua")
    fail_text = TextField(blank=True,
                          verbose_name="Thông báo được hiển thị nếu thí sinh không vượt qua")
    draft=BooleanField(verbose_name="Bản nháp", 
                       default=False)
    
    class Meta:
        verbose_name = "Ca thi"
        verbose_name_plural = "Danh sách ca thi"

    def __unicode__(self):
        return u'%s' %(self.title)
    
    def save(self, *args, **kwargs):
        # luu CaThi va Cathi_Setting
#         super(CaThi, self).save(*args, **kwargs)
#         # lay danh sach cau hoi cho ca thi
#         # lay cathi_setting
        questionGroup_settings = QuestionGroup_Setting.objects.filter(ca_thi__exact=self)
#         # cac cau hoi cua de thi
        questions = []
        for cathi_setting in questionGroup_settings:
            # lay cau hoi theo nhom va loai (type)
            qs = Question.objects.filter(mon_thi=self.monHoc,
                                    question_type = cathi_setting.loaiCauHoi,
                                    question_group = cathi_setting.level)
            # lay id
            q_ids = qs.values_list('id', flat=True)
            # lay ngau nhien so cau hoi
             
            questions += sample(q_ids, cathi_setting.num_of_questions)
         
        self.ds_cau_hoi = ','.join(map(str, questions)) + ","
         
        # luu CaThi-ds_cauhoi
        super(CaThi, self).save(*args, **kwargs)
        # tao de thi cho tung sinh vien
 
        # lay danh sach sinh vien cua lop
#         dsSV = SinhVien.objects.filter(lop=self.lop_thi)
        dsSV = self.ds_thisinh.all()
         
        if(self.tao_moi_de_thi == False):
            return
         
        # voi moi sinh vien, tao mot de thi
        for sv in dsSV:
            # tao de thi
            dethi = DeThi.objects.update_or_create(sinh_vien=sv,
                                                   ca_thi=self,
                                                   )[0]
            # lay ngau nhien cau hoi trong ngan hang de
            ds_cauhoi = sample(questions, len(questions))
            ds_cauhoi_answer = []
            for cauhoi_id in ds_cauhoi:
                # lay cau hoi voi id tuong ung
                q = Question.objects.get(id=cauhoi_id)
                # neu cau hoi la multichoice question thi hoan doi thu tu
                # cau tra loi
                if q.loaiCauHoi == MCQUESTION:
                    # lay cac cau tra loi cua cau hoi nay
#                     q = (MCQuestion)q
                     
#                     answers = Answer.objects.filter(question=q.id)
                    q.__class__ = MCQuestion
                    answers = q.getAnswers()
                     
                    # lay id cua cac cau hoi
                    answer_ids = answers.values_list('id', flat=True)
                     
                    # dao thu tu cau tra loi
                    answer_ids = sample(answer_ids, len(answer_ids))
                     
                    # add vao mot dictionary
                    ds_cauhoi_answer.append((cauhoi_id, answer_ids))
                 
                elif q.loaiCauHoi == TFQUESTION:
                    ds_cauhoi_answer.append((cauhoi_id, [1, 0]))
                 
                else:
                    ds_cauhoi_answer.append((cauhoi_id, []))
                     
            dethi.ds_cau_hoi =  json.dumps(ds_cauhoi_answer)
            dethi.save()                             
            
class QuestionGroup_Setting(models.Model):
    ca_thi = ForeignKey(CaThi, verbose_name="Ca thi")
    
    level = ForeignKey(QuestionGroup, 
                                verbose_name="Nhóm câu hỏi")
    
    loaiCauHoi = CharField(max_length=5,
                            choices=QUESTION_TYPES,
                            default=MCQUESTION,
                            verbose_name="Loại câu hỏi")
    
    mark_per_question = PositiveIntegerField(verbose_name="Điểm cho mỗi câu hỏi", 
                                             default=1) 
    num_of_questions = PositiveIntegerField(verbose_name="số câu hỏi",
                                            default=1)
    
    class Meta:
        verbose_name = "Cấu hình ca thi"
        verbose_name_plural = "Cấu hình ca thi"
#         managed=False
        
    def __unicode__(self):
        return u'%s:%s:%s' %(self.level.name,
                             self.num_of_questions,
                             self.mark_per_question)

class Chapter_Setting(models.Model):
    ca_thi = ForeignKey(CaThi, verbose_name="Ca thi")
            
    chapter = PositiveIntegerField(verbose_name="Chương", 
                                             default=1,
                                             help_text="ví dụ: 1,2,...") 
    num_of_questions = PositiveIntegerField(verbose_name="số câu hỏi",
                                            default=1)
    
    class Meta:
        verbose_name = "Thiết lập số câu hỏi cho từng chương"
        verbose_name_plural = "Thiết lập số câu hỏi cho từng chương"
#         managed=False
        
    def __unicode__(self):
        return u'%s:%s' %(self.chapter,
                             self.num_of_questions)
    
            
class Question(models.Model):
    '''
    base class for all other type of questions
    shared all properties
    '''
    monHoc = ForeignKey(MonThi,
                         blank=False, null=False,
                         verbose_name="Môn thi")
    doiTuong = ForeignKey(DoiTuong, 
                          verbose_name="Đối tượng")
    loaiCauHoi = CharField(max_length=5,
                              choices=QUESTION_TYPES,
                            default=MCQUESTION,
                            verbose_name="Loại câu hỏi")
    taoBoi = ForeignKey(GiaoVien,
                        verbose_name="Người tạo")
    
    prior = ForeignKey(QuestionGroup,
                       verbose_name="Nhóm câu hỏi",
                       related_name='prior_knowledge')
    
    level = PositiveIntegerField(default=1)
    
    thuocChuong = CommaSeparatedIntegerField(max_length=50,
                                             verbose_name="Phủ các chương",
                                             default=1)

    noiDung = models.TextField(max_length=1000,
                               blank=False,
                               verbose_name='Câu hỏi')
        
    figure = models.ImageField(upload_to='uploads/figs/%Y/%m/%d',
                               blank=True,
                               null=True,
                               verbose_name=("Ảnh"))

#     audio = models.ImageField(upload_to='uploads/audios/%Y/%m/%d',
#                                blank=True,
#                                null=True,
#                                verbose_name=("Audio"))
# 
#     clip = models.ImageField(upload_to='uploads/clips/%Y/%m/%d',
#                                blank=True,
#                                null=True,
#                                verbose_name=("Clips"))
#     
    class Meta:
        verbose_name = "Câu hỏi"
        verbose_name_plural = "Danh sách câu hỏi"
    
    def __unicode__(self):
        return u'%s' %(self.noiDung)
    
    def getAnswers(self):
        pass


class MCQuestion(Question):
    answerOrder = CharField(
        max_length=30, null=True    , blank=True,
        choices=ANSWER_ORDER_OPTIONS,
#         help_text=_("The order in which multichoice "
#                     "answer options are displayed "
#                     "to the user"),
        verbose_name="Thứ tự hiển thị câu trả lời")
    
    def save(self, *args, **kwargs):
        self.loaiCauHoi = MCQUESTION
        super(MCQuestion, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Câu hỏi loại Multiple choice"
        verbose_name_plural = "Danh sách câu hỏi loại Multiple choice"
        
    def getAnswers(self):
        return Answer.objects.filter(question=self.id)

class Answer(models.Model):
    question = ForeignKey(MCQuestion, verbose_name="Câu hỏi")

    dapAn = CharField(max_length=1000,
                               blank=False,
#                                help_text=_("Enter the answer text that "
#                                            "you want displayed"),
                               verbose_name="Phương án trả lời")

    isCorrect = BooleanField(blank=False,
                                  default=False,
                                  help_text="Phương án đúng?",
                                  verbose_name="Là phương án đúng")

    def __unicode__(self):
        return u'%s' %(self.dapAn)

    class Meta:
        verbose_name = "Phương án trả lời"
        verbose_name_plural = "Danh sách phương án trả lời"

# class EssayQuestion(Question):
#     answer = TextField(blank=False, null=False,
#                        verbose_name="Trả lời")
#     
#     def save(self, *args, **kwargs):
#         self.loaiCauHoi = ESSAYQUESTION
#         super(EssayQuestion, self).save(*args, **kwargs)
#         
#     class Meta:
#         verbose_name = "Câu hỏi tự luận"
#         verbose_name_plural = "Danh sách câu hỏi tự luận"
        
class TFQuestion(Question):
    isTrue = BooleanField(blank=False,
                                  default=False,
                                  verbose_name="Là đáp án đúng?")
    
    def save(self, *args, **kwargs):
        self.loaiCauHoi = TFQUESTION
        super(TFQuestion, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Câu hỏi Đúng/Sai"
        verbose_name_plural = "Danh sách câu hỏi Đúng/Sai"
        ordering = ['monHoc']
        
        
class DeThi(models.Model):
    sinh_vien = ForeignKey(SinhVien,
                           blank=False,
                           null=False,
                           verbose_name="Sinh Viên")
    ca_thi = ForeignKey(CaThi,
                        blank=False, null=False,
                        verbose_name="Ca thi")
    
    ds_cau_hoi = TextField(blank=False, null=False,
                           default={}, 
                           verbose_name="Danh sach cau hoi")
    
    user_answers = TextField(blank=True, default={},
                             verbose_name ="Danh sach cau tra loi cua thi sinh")
    
    complete = BooleanField(default=False, blank=False,
                            verbose_name = "Da hoan thanh bai thi chua?")
    
    start = models.DateTimeField(auto_now_add=True,
                                 verbose_name="Bat dau luc")

    end = models.DateTimeField(null=True, blank=True, 
                               verbose_name="Ket thuc luc")

    diem = PositiveIntegerField(default=0, blank=False,
                                verbose_name="Diem thi")
    
    def get_ds_cau_hoi(self):
        ds_cau_hoi = json.loads(self.ds_cau_hoi)
        
        questions = []
        
        for cau_hoi in ds_cau_hoi:
            # get cau hoi
            q = Question.objects.get(id=cau_hoi[0])

            # get cau tra loi            
            if q.loaiCauHoi == ESSAYQUESTION:
                questions.append((q, []))
            elif q.loaiCauHoi == TFQUESTION:
                questions.append((q,[True, False]))
            else:
                # get mc answers
                answers = Answer.objects.filter(question__exact=q.id)
                questions.append((q, answers))
                
        return questions

class LogSinhDe(models.Model):
    monHoc = ForeignKey(MonThi,
                        verbose_name="Môn thi")
    doiTuong = ForeignKey(DoiTuong,
                          verbose_name="Đối tượng")
    soLuong = PositiveIntegerField(verbose_name="Số lượng", 
                                   default=20)
    ngayTao = DateField(verbose_name="Ngày tạo")
    
    nguoiTao = ForeignKey(User, verbose_name="Người tạo")
    
    class Meta:
        verbose_name="Sinh đề thi"
        verbose_name_plural="Sinh đề thi"
        
    def __unicode__(self):
        return u"sinh %d đề cho môn %s, đối tượng %s" %(self.soLuong, self.monHoc, self.doiTuong)
        
    def sinhDe(self):
        '''
        sinh so luong de thi theo yeu cau cho mon thi va doi tuong da chon.
        De sinh ra phai theo cau hinh va phu noi dung chuong trinh. Cac de sinh ra
        duoc luu vao NganHangDe
        '''
        configs = self.sinhdeconf_set.all()
        message = 'Successful'
        # sinh tung de thi
        for _ in xrange(self.soLuong):
            ds_cauhoi = []
            # lay cau hoi cho tung cau hinh
            for config in configs:
                # get all question that satisfy this config
                qs = Question.objects.filter(monHoc=self.monHoc).filter(doiTuong=self.doiTuong).filter(prior=config.level).filter(loaiCauHoi=config.loaiCauHoi)
                # randomly select a number of question
                if len(qs) < config.soLuong:
#                     message = u"Số lượng câu hỏi môn %s loại %s cấp độ %d không đủ %d như cấu hình sinh đề!" %(self.monHoc, config.loaiCauHoi, config.level, config.soLuong)
                    message=u'Số lượng câu hỏi chưa đủ'
                    return False, message
                
                else:
                    ds_cauhoi += random.sample(qs, config.soLuong)
                    
            # make new NganHangDe and add these questions in to 
            nh = NganHangDe()
            nh.logSinhDe = self
            nh.daDuyet = False
            nh.questions = ','.join([str(q.pk) for q in ds_cauhoi])
            nh.save()
            nh.maDeThi = "%s%d" %(self.monHoc.ma_mon_thi, nh.pk)
            nh.save()
        return True, message
    
class SinhDeConf(models.Model):
    logSinhDe = ForeignKey(LogSinhDe)
    level = ForeignKey(QuestionGroup, 
                                verbose_name="Nhóm câu hỏi")
    
    loaiCauHoi = CharField(max_length=5,
                            choices=QUESTION_TYPES,
                            default=MCQUESTION,
                            verbose_name="Loại câu hỏi")
    
    soLuong = PositiveIntegerField(verbose_name="số câu hỏi",
                                            default=1)
    
    class Meta:
        verbose_name = "Cấu hình ca thi"
        verbose_name_plural = "Cấu hình ca thi"
#         managed=False
        
    def __unicode__(self):
        return u'%s:%s' %(self.level.name,
                             self.soLuong)
    
class NganHangDe(models.Model):
    maDeThi = CharField(max_length=10, blank=True, null=True,
                        verbose_name="Mã đề thi")
    questions = CommaSeparatedIntegerField(max_length=50,
                                           verbose_name = "Danh sách câu hỏi",
                                           default=1)
    logSinhDe = ForeignKey(LogSinhDe)
    
    daDuyet = BooleanField(verbose_name="Đã duyệt",
                           default=False)
    
    ngay_tao = DateField(verbose_name="Ngày tạo")
    
    class Meta:
        verbose_name="Ngân hàng đề thi"
        verbose_name_plural="Ngân hàng đề thi"
        
    def bocVaTronDe(self, idMonHoc, idDoiTuong, soLuong):
        '''
        Boc de thi trong ngan hang de theo mon hoc va doi tuong.
        Sau khi co de thi, tien hanh tron de thi thanh (soLuong) de
        '''
        pass