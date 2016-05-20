# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.db.models.fields import CharField, TextField, DateField, TimeField,\
    CommaSeparatedIntegerField, BooleanField, PositiveIntegerField, FloatField,\
    DurationField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from hrm.models import GiaoVien, DonVi
from random import sample
from hvhc import MCQUESTION, TFQUESTION, QUESTION_TYPES, ANSWER_ORDER_OPTIONS,\
    ESSAYQUESTION, HOC_KY, HK1, TRANG_THAI_THI, TRANG_THAI_KHTHI, KHTHI_CHUATHI,\
    PERM_BOC_DE, PERM_XEM_IN_DE
import json
from daotao.models import Lop, MonThi, DoiTuong, SinhVien
import random
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in, user_logged_out
from openpyxl.reader.excel import load_workbook
from django.forms.fields import DecimalField
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


# class QuestionGroup_Setting(models.Model):
#     ca_thi = ForeignKey(CaThi, verbose_name="Ca thi")
#
#     level = ForeignKey(QuestionGroup,
#                                 verbose_name="Nhóm câu hỏi")
#
#     loaiCauHoi = CharField(max_length=5,
#                             choices=QUESTION_TYPES,
#                             default=MCQUESTION,
#                             verbose_name="Loại câu hỏi")
#
#     mark_per_question = PositiveIntegerField(verbose_name="Điểm cho mỗi câu hỏi",
#                                              default=1)
#     num_of_questions = PositiveIntegerField(verbose_name="số câu hỏi",
#                                             default=1)
#
#     class Meta:
#         verbose_name = "Cấu hình ca thi"
#         verbose_name_plural = "Cấu hình ca thi"
# #         managed=False
#
#     def __unicode__(self):
#         return u'%s:%s:%s' %(self.level.name,
#                              self.num_of_questions,
#                              self.mark_per_question)
#
# class Chapter_Setting(models.Model):
#     ca_thi = ForeignKey(CaThi, verbose_name="Ca thi")
#
#     chapter = PositiveIntegerField(verbose_name="Chương",
#                                              default=1,
#                                              help_text="ví dụ: 1,2,...")
#     num_of_questions = PositiveIntegerField(verbose_name="số câu hỏi",
#                                             default=1)
#
#     class Meta:
#         verbose_name = "Thiết lập số câu hỏi cho từng chương"
#         verbose_name_plural = "Thiết lập số câu hỏi cho từng chương"
# #         managed=False
#
#     def __unicode__(self):
#         return u'%s:%s' %(self.chapter,
#                              self.num_of_questions)


class Question(models.Model):
    '''
    base class for all other type of questions
    shared all properties
    '''
    maCauHoi = CharField(max_length=20, verbose_name="Mã câu hỏi", unique=True)

    monHoc = ForeignKey(MonThi,
                         blank=False, null=False,
                         verbose_name="Môn thi")
    doiTuong = ForeignKey(DoiTuong,
                          verbose_name="Đối tượng")
    loaiCauHoi = CharField(max_length=5,
                              choices=QUESTION_TYPES,
                            default=MCQUESTION,
                            verbose_name="Loại câu hỏi")
#     taoBoi = ForeignKey(GiaoVien,
#                         verbose_name="Người tạo")

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

    diem = FloatField(verbose_name="Điểm", default=1.0)

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
        return u'%d' %(self.pk)

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


# class DeThi(models.Model):
#     sinh_vien = ForeignKey(SinhVien,
#                            blank=False,
#                            null=False,
#                            verbose_name="Sinh Viên")
#     ca_thi = ForeignKey(CaThi,
#                         blank=False, null=False,
#                         verbose_name="Ca thi")
#
#     ds_cau_hoi = TextField(blank=False, null=False,
#                            default={},
#                            verbose_name="Danh sach cau hoi")
#
#     user_answers = TextField(blank=True, default={},
#                              verbose_name ="Danh sach cau tra loi cua thi sinh")
#
#     complete = BooleanField(default=False, blank=False,
#                             verbose_name = "Da hoan thanh bai thi chua?")
#
#     start = models.DateTimeField(auto_now_add=True,
#                                  verbose_name="Bat dau luc")
#
#     end = models.DateTimeField(null=True, blank=True,
#                                verbose_name="Ket thuc luc")
#
#     diem = PositiveIntegerField(default=0, blank=False,
#                                 verbose_name="Diem thi")
#
#     def get_ds_cau_hoi(self):
#         ds_cau_hoi = json.loads(self.ds_cau_hoi)
#
#         questions = []
#
#         for cau_hoi in ds_cau_hoi:
#             # get cau hoi
#             q = Question.objects.get(id=cau_hoi[0])
#
#             # get cau tra loi
#             if q.loaiCauHoi == ESSAYQUESTION:
#                 questions.append((q, []))
#             elif q.loaiCauHoi == TFQUESTION:
#                 questions.append((q,[True, False]))
#             else:
#                 # get mc answers
#                 answers = Answer.objects.filter(question__exact=q.id)
#                 questions.append((q, answers))
#
#         return questions

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
        nhde = NganHangDe.objects.filter(logSinhDe__monHoc=self.monHoc, logSinhDe__doiTuong=self.doiTuong, daDuyet=True)
        ds_dethi_daco = []
        for dethi in nhde:
            qs = [int(q_id) for q_id in dethi.questions.split(',')]
            ds_dethi_daco.append(set(qs))

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
                    while True:
                        ds_cauhoi += random.sample(qs, config.soLuong)
                        ds_cauhoi_id = [q.id for q in ds_cauhoi]
                        set_cauhoi = set(ds_cauhoi_id)

                        # check trung voi de trong ngan hang da co
                        if len(ds_dethi_daco) == 0:
                            break

                        ok = False
                        for dethi in ds_dethi_daco:
                            if len(set_cauhoi.difference(dethi)) > 0:
                                ok = True
                                break
                        if ok:
                            break
            # make new NganHangDe and add these questions in to
            nh = NganHangDe()
            nh.logSinhDe = self
            nh.daDuyet = False
            nh.ngay_tao = timezone.now()
            nh.questions = ','.join([str(q.pk) for q in ds_cauhoi])
            nh.save()
            nh.maDeThi = "%s%d" %(self.monHoc.ma_mon_thi, nh.pk)
            print nh.maDeThi
            nh.save()
        return True, message

class SinhDeConf(models.Model):
    logSinhDe = ForeignKey(LogSinhDe, verbose_name="Cấu hình sinh đề")
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
    logSinhDe = ForeignKey(LogSinhDe, verbose_name="Cấu hình sinh đề")

    daDuyet = BooleanField(verbose_name="Đã duyệt",
                           default=False)

    ngay_tao = DateField(verbose_name="Ngày tạo")

    class Meta:
        verbose_name="Ngân hàng đề thi"
        verbose_name_plural="Ngân hàng đề thi"


class KHThi(models.Model):
    '''
    Thiet lap mot ca thi, trong do co danh sach cau hoi de tu do lam
    cac de thi cho tung sinh vien
    '''
    ten = CharField(verbose_name=u"Tên", max_length=200, blank=False)

    nam_hoc = CharField(max_length=9,
                        verbose_name=u"Năm học",
                        help_text=u"Nhập năm học theo định dạng XXXX-XXXX. Ví dụ 2015-2016")

    hoc_ky = CharField(max_length=3,
                              choices=HOC_KY,
                            default=HK1,
                            verbose_name=u"Học kỳ")

    doi_tuong = ForeignKey(DoiTuong,
                           verbose_name=u"Đối tượng")

    mon_thi = ForeignKey(MonThi, blank=False, null=False,
                         related_name='%(class)s_monthi_cathi',
                         verbose_name="Môn thi")

    ds_giamthi = ManyToManyField(GiaoVien, related_name='%(class)s_giamthi_khthi',
                                 verbose_name=u'Danh sách giám thị coi thi')

    ds_thisinh = ManyToManyField(SinhVien, blank=False, related_name='%(class)s_sinhvien_khthi',
                                verbose_name=u'Danh sách thí sinh')
#     ds_thisinh.help_text = u'Tìm kiếm theo họ tên sinh viên hoặc mã lớp.'

    ngay_thi = DateField(verbose_name="Ngày thi", default=timezone.now)
    tg_bat_dau=TimeField(verbose_name="Thời gian bắt đầu", default=timezone.now)
#     tg_ket_thuc=TimeField(verbose_name="Thời gian kết thúc")
    tg_thi = PositiveIntegerField(verbose_name="Thời gian thi (phút)", default=30, help_text="Nhập thời gian thi tính bằng đơn vị phút")

    tg_thi_batdau = TimeField(default=timezone.now)

    de_thi_id = PositiveIntegerField(null=True)

    de_thi = TextField(default=json.dumps({}))
    # dict id cau hoi: id dap an dung
    dap_an = TextField(default=json.dumps({}))

    tao_moi_de_thi = BooleanField(blank=False, null=False,
                                  verbose_name="Tạo mới đề thi cho các sinh viên",
                                  default=True)

    so_luong_de = PositiveIntegerField(verbose_name="Số lượng đề thi tạo ra", default=0)
    so_luong_de.help_text = u'Nhập giá trị >= 0, nhập 0 sẽ sinh mỗi sinh viên một đề'
    ghichu=TextField(verbose_name="Ghi chú", blank=True, null=True)

    nguoi_boc_de = ForeignKey(GiaoVien, verbose_name="Người bốc đề", null=True, blank=True)
    trang_thai =  CharField(max_length=30, null=True, blank=True,
        choices=TRANG_THAI_KHTHI, default=KHTHI_CHUATHI, verbose_name='Trạng thái')

    class Meta:
        verbose_name = u"Kế hoạch thi - bốc đề"
        verbose_name_plural = u"Kế hoạch thi - bốc đề"
        permissions = ((PERM_BOC_DE, 'Người dùng được phép bốc đề'),
                        (PERM_XEM_IN_DE, 'Người dùng được phép xem và in đề'),)

    def __unicode__(self):
        return u'%s' %(self.ten)

    def boc_va_tron_de(self, nguoi_boc_de):
        '''
        Boc de thi trong ngan hang de theo mon hoc va doi tuong.
        Sau khi co de thi, tien hanh tron de thi thanh (soLuong) de
        '''
        self.nguoi_boc_de = nguoi_boc_de

        ngan_hang_de = NganHangDe.objects.filter(logSinhDe__monHoc=self.mon_thi).filter(logSinhDe__doiTuong=self.doi_tuong).filter(daDuyet=True)
        if len(ngan_hang_de)==0:
            return False
        # boc de
        de_thi = random.choice(ngan_hang_de)
        self.de_thi_id = de_thi.id

        id_cauhois = de_thi.questions.split(',')
        de_thi_dict = {}
        dap_an_dict={}
        for id_cauhoi in id_cauhois:
            cauhoi = Question.objects.get(pk = id_cauhoi)
            answers = Answer.objects.filter(question=cauhoi)
            de_thi_dict[id_cauhoi] = []
            for a in answers:
                de_thi_dict[id_cauhoi].append(a.id)
                if a.isCorrect:
                    dap_an_dict[id_cauhoi] = a.id
        self.de_thi = json.dumps(de_thi_dict)
        self.dap_an = json.dumps(dap_an_dict)
        self.save()

        # tron de cho tung sinh vien tham gia
        # delete old records for this khthi
        bts = BaiThi.objects.filter(khthi=self)
        for bt in bts:
            bt.delete()

        ds_thisinh = self.ds_thisinh.all()
        for sv in ds_thisinh:
#             bts = BaiThi.objects.filter(khthi = self).filter(thi_sinh=sv)
#             for bt in bts:
#                 bt.delete()
            bai_thi = BaiThi()
            bai_thi.khthi = self
            bai_thi.thi_sinh = sv
            ds_cauhoi = []
            q_ids = random.sample(id_cauhois, len(id_cauhois))
            for q_id in q_ids:
                ds_cauhoi.append([q_id, random.sample(de_thi_dict[q_id], len(de_thi_dict[q_id]))])
            bai_thi.ds_cauhoi = json.dumps(ds_cauhoi)
            bai_thi.tra_loi = {}
            bai_thi.diem = 0
            bai_thi.save()

        return True

    def get_ds_baithi(self):
        '''
        return {baithi: [[cauhoi,[phuong an tra loi]]]}}
        '''
        ds_baithi_dict = {}

        ds_baithi = BaiThi.objects.filter(khthi=self)

        for baithi in ds_baithi:
            ds_cauhoi = json.loads(baithi.ds_cauhoi)
            ds_baithi_dict[baithi] = []
            for qid, pa_ids in ds_cauhoi:
                q = Question.objects.get(pk=qid)
                pas = []
                for pa_id in pa_ids:
                    pas.append(Answer.objects.get(pk=pa_id))

                ds_baithi_dict[baithi].append([q, pas])

        return ds_baithi_dict


class BaiThi(models.Model):
    '''
    Bai thi cua moi sinh vien cho tung mon
    '''
    khthi = ForeignKey(KHThi)
    thi_sinh = ForeignKey(SinhVien, verbose_name="Sinh viên", to_field='ma_sv')
    ds_cauhoi = TextField(default={})
    tra_loi = TextField(default={})
    diem = FloatField(verbose_name="Điểm")
    is_finished = BooleanField(default=False, verbose_name="Hoàn thành")



    class Meta:
        verbose_name = u'Bài thi'
        verbose_name_plural = u"Bài thi"
        unique_together = ("khthi", "thi_sinh")

    def __unicode__(self):
        return u'%s' %(self.thi_sinh.get_ho_ten)

    def cham_diem(self):
        tra_loi_dict = json.loads(self.tra_loi)
        dap_an_dict = json.loads(self.khthi.dap_an)
        diem = 0
        for k,v in tra_loi_dict.items():
            if dap_an_dict[k] == v:
                q = Question.objects.get(pk=k)
                diem += q.diem

        self.diem = diem
        self.save()

    def finish(self):
        self.is_finished = True
        self.save()

    def get_ds_cauhoi(self):
        '''
        return [[cau_hoi,[pa1, pa2, pa3, pa4]], ....[..]]
        '''
        ds_cauhoi_list = []
        ds_cauhoi = json.loads(self.ds_cauhoi)

        for i in xrange(len(ds_cauhoi)):
            cauhoi_id, pa_ids = ds_cauhoi[i]

            cauhoi = Question.objects.get(pk = cauhoi_id)

            answers = []
            for j in xrange(len(pa_ids)):
                pa_id = pa_ids[j]
                pa = Answer.objects.get(pk=pa_id)
                answers.append(pa)

            ds_cauhoi_list.append([cauhoi, answers])
        return ds_cauhoi_list

    def get_traloi(self):
        '''
        return {question_id: answer_id}
        '''
        traloi_dict = json.loads(self.tra_loi)

        return traloi_dict
    def get_dapan(self):
        dap_an_dethi =  json.loads(self.khthi.dap_an)
        ds_cauhoi = json.loads(self.ds_cauhoi)

        # {cauhoi (1..): [A, B, C, D] }
        dap_an_baithi = {}
        pa_letters = ['A', 'B', 'C', 'D']

        # foreach cau hoi
        for i in xrange(len(ds_cauhoi)):
            cauhoi_id, pa_ids = ds_cauhoi[i]
            # chon dap an dung
            id_dapan = dap_an_dethi[cauhoi_id]
            for pa_id, pa_letter in zip(pa_ids, pa_letters):
                if pa_id == id_dapan:
                    dap_an_baithi[str(i+1)] = pa_letter
                    break

        return dap_an_baithi

    def save_tralois(self, traloi_dict):
        self.tra_loi = json.dumps(traloi_dict)
        self.save()

    def update_traloi(self, question_id, answer_id):
        traloi = json.loads(self.tra_loi)
        traloi[question_id] = answer_id
        self.tra_loi = json.dumps(traloi)
        self.save()


    def in_bai_thi(self):
        pass

class LoggedUser(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    login_time = models.DateTimeField()

    def __unicode__(self):
        return self.username

class ImportMCQuestion(models.Model):
    '''
    The hien cho 1 de thi tu luan
    '''
    mon_thi = models.ForeignKey(MonThi,
                                  verbose_name="Môn thi")

    doi_tuong = models.ForeignKey(DoiTuong, verbose_name="Đối tượng")

#     khoa = models.ForeignKey(DonVi, verbose_name="Khoa")
    import_file = models.FileField(upload_to='tmp',
                               blank=True,
                               null=True,
                               verbose_name=("Chọn file dữ liệu"))
    class Meta:
        verbose_name = u'Nhập danh sách câu hỏi Multiple Choice từ file'
        verbose_name_plural = u"Nhập danh sách câu hỏi Multiple Choice từ file"

    def import_data(self):
        wb = load_workbook(filename=self.import_file.path)
        ws = wb.active
        for row in ws.rows[1:]:
            if row[0].value == None:
                break

            try:
                mcq = MCQuestion()
                mcq.maCauHoi = row[0].value
                mcq.noiDung = row[1].value
                mcq.diem = row[6].value
#                 mcq.taoBoi=row[7].value

                mcq.doiTuong = self.doi_tuong
                mcq.monHoc = self.mon_thi
                mcq.level=1
                mcq.prior_id=1
                mcq.loaiCauHoi=MCQUESTION
                mcq.thuocChuong='1'
                mcq.save()
                # for answer
                for i in xrange(2,6):
                    if len(row[i].value)==0:
                        continue
                    a = Answer()
                    a.dapAn = row[i].value
                    a.question = mcq
                    if i == 2:
                        a.isCorrect = 1
                    a.save()
            except Exception, e:
                print str(e)
                continue


def login_user(sender, request, user, **kwargs):
    LoggedUser(username=user.username, login_time=timezone.now()).save()

def logout_user(sender, request, user, **kwargs):
    if not user:
        return
    try:
        u = LoggedUser.objects.get(username=user.username)
        u.delete()
    except LoggedUser.DoesNotExist:
        pass

user_logged_in.connect(login_user)
user_logged_out.connect(logout_user)
