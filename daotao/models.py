# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
# from hrm.models import SinhVien
from django.db.models.fields import CharField, CommaSeparatedIntegerField, PositiveIntegerField
# from hvhc import TRANG_THAI_THI
# import hvhc
from hvhc import TRANG_THAI_THI
from django.contrib.auth.models import User
from hrm.models import DonVi

# from hrm.models import DonVi
# from hrm.models import SinhVien
# import hrm

class DoiTuong(models.Model):
    ma_dt = CharField(unique=True, max_length=10,
                      verbose_name="Mã đối tượng")
                      
    ma_dt.help_text = "Mã không quá " + str(ma_dt.max_length)+" ký tự"
    
    ten_dt = CharField(unique=True, max_length=50,
                       verbose_name = 'Tên đối tượng')
    
    class Meta:
        verbose_name="Đối tượng"
        verbose_name_plural="Danh sách đối tượng"
        
    def __unicode__(self):
        return u'%s(%s)' %(self.ten_dt, self.ma_dt)
    
# @python_2_unicode_compatible
class MonThi(models.Model):
    ma_mon_thi = CharField(verbose_name = "Mã môn thi", unique = True, max_length=10)
    ten_mon_thi = CharField(verbose_name = "Môn thi", unique=True,max_length=200) 
    so_chuong = PositiveIntegerField(verbose_name="Số chương", default=5)
    so_dvht = PositiveIntegerField(verbose_name="Số đơn vị học trình", default=3)
    khoa = ForeignKey(DonVi, verbose_name="Khoa")
    
    class Meta:
        verbose_name = "Môn thi"
        verbose_name_plural = "Danh sách môn thi"
        
    def __unicode__(self):
        return u'%s - %s' %(self.ten_mon_thi, self.khoa.ma_dv)
     
# @python_2_unicode_compatible
class Lop(models.Model):
    ma_lop = CharField(verbose_name="Mã lớp", unique=True, max_length=5)
    ten_lop = CharField(verbose_name = "Lớp", unique=True, max_length=200)
    si_so = PositiveIntegerField(verbose_name="Sĩ số", blank=True,null=True)
    doi_tuong = ForeignKey(DoiTuong, verbose_name="Đối tượng", 
                           blank=False, null=False)

    class Meta:
        verbose_name = "Lớp"
        verbose_name_plural = "Danh sách lớp"
    
    def __unicode__(self):
        return u'%s' %(self.ten_lop)
    
class SinhVien(models.Model):
    user = OneToOneField(User)
    ma_sv=PositiveIntegerField(blank=False, null=False,
                               unique=True,
                               verbose_name="Mã sinh viên")
    ho_ten = CharField(blank=False, null=False,
                       max_length=50,
                       verbose_name="Họ và tên")
    lop = ForeignKey(Lop, blank=False, null=False,
                     verbose_name="Lớp")
    # tam the da, co the can them cac truong khac
    

    class Meta:
        verbose_name = "Sinh viên"
        verbose_name_plural = "Danh sách sinh viên"

    def __unicode__(self):
        return u'%s-%s' %(self.ho_ten, self.lop.ma_lop)
    
    def save(self, *args, **kwargs):
        '''
        when save a student, we also make a user who can login to make exam
        '''
#         print self.ma_sv
        u = User.objects.filter(username=self.ma_sv)
        if len(u) == 0: 
            new_user = User.objects.create_user(username=self.ma_sv, password=self.ma_sv)
            new_user.is_staff = True
            new_user.save()
            self.user = new_user
        else:
            self.user = u[0];
        super(SinhVien, self).save(*args, **kwargs)
        
    def delete(self, using=None):
        '''
        also delete from user table
        '''
        user = User.objects.get_by_natural_key(self.ma_sv)
        User.delete(user, using)
        models.Model.delete(self, using=using)
        
class Diem(models.Model):
    sinh_vien=ForeignKey(SinhVien,
                         blank=False, null=False, 
                         verbose_name="Sinh viên")
    mon_thi = ForeignKey(MonThi,
                         blank=False, null=False,
                         verbose_name="Môn thi")
    
    trang_thai_thi = CharField(max_length=20,
                               choices=TRANG_THAI_THI,
                               default='DA_THI',
                               verbose_name='Trạng thái thi')
    
    diem=CommaSeparatedIntegerField(max_length=5, blank=True, null=True,
                              verbose_name="Điểm")
    class Meta:
        unique_together = (('sinh_vien', 'mon_thi'),)
        verbose_name = "Điểm"
        verbose_name_plural = "Bảng điểm"
        

