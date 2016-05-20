'''
Created on Jan 17, 2016

@author: pta
'''
from daotao import views
from django.conf.urls import url

urlpatterns = [
    url(r'^import/sinhvien/(?P<pk>[\d]+)/$', views.import_sinhvien, name='import sinhvien data'),
]