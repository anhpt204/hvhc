
from django.conf.urls import url
from tracnghiem import views
from tracnghiem.views import CathiDetailView, DethiStartView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login_user'),
    
    url(r'^cathi/(?P<pk>[\d]+)/$', CathiDetailView.as_view(), name="cathi_detail"),
    url(r'^cathi/(?P<pk>[\d]+)/start/$', DethiStartView.as_view(), name='dethi_start'),
    url(r'^cathi/(?P<pk>[\d]+)/start/finish/$', views.quiz_finish, name='quiz_finish'),
    url(r'^sinhde/(?P<pk>[\d]+)/$', views.sinhde, name="sinh danh sach de thi"),
    url(r'^export/dethi/(?P<pk>[\d]+)/$', views.export, name="export de thi"),    
    url(r'^khthi/boctrondethi/(?P<pk>[\d]+)/$', views.boc_tron_de_thi, name="boc va tron de thi"),
    url(r'^khthi/show/(?P<pk>[\d]+)/$', views.khthi_show, name="hien thi danh sach thi sinh - de thi"),
    url(r'^khthi/show/([\d]+)/export/(?P<pk>[\d]+)/$', views.export_baithi_cauhoi, name="export bai thi cua tung thi sinh"),

]