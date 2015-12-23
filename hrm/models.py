# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.db import models
from django.db.models.fields.related import OneToOneField, ForeignKey
from django.db.models.fields import PositiveIntegerField, CharField
from django.contrib.auth.models import User
from daotao.models import Lop
# import hvhc

class DonVi(models.Model):
    ma_dv = CharField(verbose_name="Mã đơn vị", unique = True, max_length=5,
                      help_text="Mã đơn vị không quá 5 ký tự")
    ten_dv = CharField(verbose_name="Tên đơn vị", unique=True, max_length=200)
    
    cha_dv = ForeignKey("DonVi", verbose_name="Đơn vị cấp trên", null=True, blank=True,
                        help_text="Đơn vị cấp trên trực tiếp")
    
    class Meta:
        verbose_name = "Đơn vị"
        verbose_name_plural =   "Danh sách đơn vị"
        
    def __unicode__(self):
        if self.cha_dv:
            return u'%s - %s' %(self.ten_dv, self.cha_dv)
        else:
            return u'%s' %(self.ten_dv)
    
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
        
class GiaoVien(models.Model):
    user = OneToOneField(User)
    
    ma_so=PositiveIntegerField(blank=False, null=False,
                               unique=True,
                               verbose_name="Mã số")
    
    ho_ten = CharField(blank=False, null=False,
                       max_length=50,
                       verbose_name="Họ và tên")
    
    don_vi = ForeignKey(DonVi, verbose_name='Đơn vị', help_text="Đơn vị quản lý trực tiếp")
    
#     lop = ForeignKey(Lop, blank=False, null=False,
#                      verbose_name="Lớp")
    # tam the da, co the can them cac truong khac
    

    class Meta:
        verbose_name = "Giáo viên"
        verbose_name_plural = "Danh sách giáo viên"

    def __unicode__(self):
        return u'%s (%s)' %(self.ho_ten, self.don_vi)
    
    def save(self, *args, **kwargs):
        '''
        when save a student, we also make a user who can login to make exam
        '''
        u = 'GV'+str(self.ma_so)
        # check if this GV already exist in user table
        users = User.objects.filter(username=u)
        # if not
        if len(users) == 0:
            # then create a new user 
            new_user = User.objects.create_user(username=u, password=self.ma_so)
            new_user.is_staff = True
            new_user.save()
            self.user = new_user
        else:
            self.user = users[0];
        super(GiaoVien, self).save(*args, **kwargs)
        
    def delete(self, using=None):
        '''
        also delete from user table
        '''
        user = User.objects.get_by_natural_key(self.ma_so)
        User.delete(user, using)
        models.Model.delete(self, using=using)
