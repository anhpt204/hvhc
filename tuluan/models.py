# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.db import models
from django.db.models.fields import CharField, DateField, PositiveIntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from daotao.models import DoiTuong, MonThi, Lop
from django.utils import timezone
from hvhc import HOC_KY, HK1
from hrm.models import GiaoVien
from datetime import date

class BoDe(models.Model):
    '''
    Bo de thi tu luan
    '''
    ma_so = CharField(max_length=20, unique=False, blank=True, null=True,
                    verbose_name="Mã bộ đề")
    
    doi_tuong = ForeignKey(DoiTuong,
                           blank=False, null=False,
                           verbose_name="Đối tượng thi")
    
    mon_thi = ForeignKey(MonThi,
                         blank=False, null=False,
                         verbose_name="Môn thi")
    ngay_tao = models.DateField('Ngày tạo', default=timezone.now)
    
    class Meta:
        verbose_name='Bộ đề thi tự luận'
        verbose_name_plural="Bộ đề thi tự luận"
    
    def __unicode__(self):
        return u'%s(%s)' %(self.mon_thi, self.doi_tuong)
    
    
    def save(self, *args, **kwargs):
        self.ma_so = '%s.%s.%s.%s.%s' %(self.doi_tuong.ma_dt, self.mon_thi.ma_mon_thi,
                                        self.ngay_tao.day, self.ngay_tao.month, self.ngay_tao.year)
        
        super(BoDe, self).save(*args, **kwargs)
        # ma = ma doi tuong.ma mon.ngay.thang.nam

#     def clone(self):
        
    
class DeThi(models.Model):
    '''
    The hien cho 1 de thi tu luan
    '''
    ngan_hang = models.ForeignKey(BoDe,
                                  verbose_name="Ngân hàng")
    
    ma_de_thi = models.CharField(max_length=10, #unique=True,
                                 verbose_name="Mã đề thi")
    
    de_thi = models.FileField(upload_to='uploads/essay/%Y/%m/%d',
                               blank=True,
                               null=True,
                               verbose_name=("Đề thi"))
    dap_an = models.FileField(upload_to='uploads/essay/%Y/%m/%d',
                               blank=True,
                               null=True,
                               verbose_name=("Đáp án"))
    class Meta:
        verbose_name="Đề thi tự luận"
        verbose_name_plural="Danh sách đề thi tự luận"
        
    def __unicode__(self):
        return u'%s (%s)' %(self.ma_de_thi, self.ngan_hang)
    
        
class CaThi(models.Model):
    ten_ca_thi = CharField(max_length=100,
                           verbose_name="Tên ca thi")
    
    nam_hoc = CharField(max_length=9,
                        verbose_name="Năm học",
                        help_text="Nhập năm học theo định dạng XXXX-XXXX. Ví dụ 2015-2016")
    
    hoc_ky = CharField(max_length=3,
                              choices=HOC_KY,
                            default=HK1,
                            verbose_name="Học kỳ")

    doi_tuong = ForeignKey(DoiTuong,
                           verbose_name="Đối tượng")
    
    mon_thi = ForeignKey(MonThi,
                         verbose_name = "Môn thi")
    
    lop = ForeignKey(Lop,
                     verbose_name = "Lớp")

    ngay_thi = DateField(verbose_name="Ngày thi")
#     
    giam_thi = ManyToManyField(GiaoVien, blank=False, 
                              verbose_name=u'Danh sách giám thị coi thi')

#     giam_thi = ManyToManyField(GiaoVien, blank=False,
#                                 verbose_name = u'GT')
    
    so_de_thi = PositiveIntegerField(verbose_name = "Số đề thi",
                                     default=1,
                                     help_text = u"Số đề thi là số nguyên dương, lớn hơn 0")
    ds_de_thi = ManyToManyField(DeThi, blank=True,
                                verbose_name = u'DT')

    class Meta:
        verbose_name = u"Kế hoạch thi - bốc đề"
        verbose_name_plural = u"Kế hoạch thi - bốc đề"

    def __unicode__(self):
        return u'%s-%s-%s' %(self.doi_tuong, self.mon_thi, self.lop)
    
    @property
    def da_thi(self):
        if date.today() < self.ngay_thi:
            return True
        return False

#     def save(self, *args, **kwargs):
#         # lay ngan hang de thi tuong ung voi doi_tuong va mon_thi
#         ngan_hang_dt = BoDe.objects.filter(doi_tuong=self.doi_tuong, 
#                                                           mon_thi=self.mon_thi)
#         # lay so_de_thi
#         de_thi_s = random.sample(ngan_hang_dt, self.so_de_thi)
#         for de_thi in de_thi_s:
#             self.ds_de_thi.add(de_thi)
#         super(CaThi, self).save(*args, **kwargs)