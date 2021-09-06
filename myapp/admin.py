from django.contrib import admin
from myapp.models import student

# Register your models here.
# 第一種方法, 未加入ModelAdmin
# admin.site.register(student)

# 第二種方法, 加入ModelAdmin
# class studentAdmin(admin.ModelAdmin):
#     list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
# admin.site.register(student,studentAdmin)

# 第三種方法, 加入ModelAdmin, 篩選, 搜尋, 排序
class studentAdmin(admin.ModelAdmin):
    list_display = ('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
    list_filter = ('cName','cSex')
    search_fields = ('cName',)
    ordering = ('id',)
admin.site.register(student,studentAdmin)