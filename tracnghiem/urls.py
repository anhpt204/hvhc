
from django.conf.urls import url
from tracnghiem import views
from tracnghiem.views import BaiThiDetailView, BaiThiStartView

urlpatterns = [
    url(r'^$', views.login_user, name='index'),
    url(r'^login/$', views.login_user, name='login_user'),
    
    url(r'^baithi/(?P<pk>[\d]+)/$', BaiThiDetailView.as_view(), name="baithi_detail"),
    url(r'^baithi/(?P<pk>[\d]+)/start/$', BaiThiStartView.as_view(), name='baithi_start'),
    url(r'^baithi/(?P<pk>[\d]+)/finish/$', views.quiz_finish, name='quiz_finish'),
    url(r'^sinhde/(?P<pk>[\d]+)/$', views.sinhde, name="sinh danh sach de thi"),
    url(r'^export/dethi/(?P<pk>[\d]+)/$', views.export, name="export de thi"),    
    url(r'^khthi/boctrondethi/(?P<pk>[\d]+)/$', views.boc_tron_de_thi, name="boc va tron de thi"),
    url(r'^khthi/show/(?P<pk>[\d]+)/$', views.khthi_show, name="hien thi danh sach thi sinh - de thi"),
    url(r'^khthi/show/([\d]+)/export/(?P<pk>[\d]+)/$', views.export_baithi_cauhoi, name="export bai thi cua tung thi sinh"),

]