'''
Created on Sep 18, 2015

@author: pta
'''

from django.conf.urls import url
from tuluan import views
from tuluan.views import CaThiView


urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^login/$', views.login_user, name='login_user'),
    
#     url(r'^cathi/(?P<pk>[\d]+)/$', CathiDetailView.as_view(), name="cathi_detail"),
#     url(r'^cathi/(?P<pk>[\d]+)/start/$', DethiStartView.as_view(), name='dethi_start'),
#     url(r'^cathi/(?P<pk>[\d]+)/start/finish/$', views.quiz_finish, name='quiz_finish'),
    url(r'^preview/(?P<pk>[\d]+)/$', views.view_pdf, name='view_pdf'),
    url(r'^preview/dethi/(?P<pk>[\d]+)/$', views.view_dethi, name='view_dethi'),
    url(r'^preview/dapan/(?P<pk>[\d]+)/$', views.view_dapan, name='view_dapan'),
    
    url(r'^get_dt/(?P<pk>[\d]+)/$', CaThiView.as_view(), name='get_dt'),
    url(r'^get_dt/(?P<pk>[\d]+)/sinhde/$', views.sinh_de, name='sinhde'),
    url(r'^print/(?P<pk>[\d]+)/$', views.print_dt, name='print'),
    
    
]