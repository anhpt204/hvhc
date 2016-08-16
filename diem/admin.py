from django.contrib import admin
from diem.models import LoaiDiem

# Register your models here.
class LoaiDiemAdmin(admin.ModelAdmin):
    model = LoaiDiem
admin.site.register(LoaiDiem, LoaiDiemAdmin)
