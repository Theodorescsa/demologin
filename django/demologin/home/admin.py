from django.contrib import admin
from .models import department, Member
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department_id','name')
    search_fields=['name']
    list_filter=('department_id','name')
admin.site.register(department, DepartmentAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display=('member_id','User','Bookname')
    search_fields=['Bookname','User']
    list_filter=('member_id','User','Bookname')
admin.site.register(Member, MemberAdmin)
