from django.contrib import admin
from .models import userinfo
# Register your models here.
class Adminuserinfo(admin.ModelAdmin):
    readonly_fields=('UID',)
    list_display = ['UID','UName']

admin.site.register(userinfo,Adminuserinfo)