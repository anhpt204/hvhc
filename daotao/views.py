# -*- encoding: utf-8 -*-
'''
Created on Jan 17, 2016

@author: pta
'''
from daotao.models import ImportSinhVien
from django.http.response import HttpResponse

def import_sinhvien(request, pk):
    import_sv = ImportSinhVien.objects.get(pk=pk)
    import_sv.import_data()
    return HttpResponse('<h1>Đã cập nhật dữ liệu xong!</h1>')