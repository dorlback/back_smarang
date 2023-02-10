from django.contrib import admin
from . import models
from ckeditor.widgets import CKEditorWidget
from django import forms

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'nickname',
        'email',
        'date_joined',
    )
    
    list_display_links = (
        'nickname',
        'email',
    )




@admin.register(models.Marketer_detail)
class Marketer_detai_adminl(admin.ModelAdmin):
    search_fields = ['marketer_id']

@admin.register(models.Brand_detail)
class Brand_detail_admin(admin.ModelAdmin):
    search_fields = ['brand_id']

@admin.register(models.POST)
class Post_admin(admin.ModelAdmin):
    search_fields = ['marketer_addr']

@admin.register(models.Notice)
class Notice_admin(admin.ModelAdmin):
    search_fields = ['notice_title']

@admin.register(models.Terms)
class Terms_admin(admin.ModelAdmin):
    search_fields = ['term_titleasd']

@admin.register(models.Brand_user)
class B_userAdmin(admin.ModelAdmin):
    search_fields = ['phoneNumber']

class Item_list_line(admin.TabularInline):
    model = models.Item_list

class Item_succ_line(admin.TabularInline):
    model = models.Item_succ

class Cal_table_line(admin.TabularInline):
    model = models.Cal_table

class Item_list_admin(admin.ModelAdmin):
    inlines=[
        Item_list_line,Item_succ_line,Cal_table_line
    ]

class Perform_list_line(admin.TabularInline):
    model = models.Perform_list

class Button_list_line(admin.TabularInline):
    model = models.Button_con


class Perform_list_admin(admin.ModelAdmin):
    inlines=[
        Perform_list_line,Button_list_line
    ]

class M_userAdmin(admin.ModelAdmin):
    inlines=[
        Item_succ_line
    ]

class Cal_data_line(admin.TabularInline):
    model = models.Cal_data

class Cal_data_table(admin.ModelAdmin):
    inlines=[
        Cal_data_line
    ]

#버튼 
class Button_line(admin.TabularInline):
    model = models.Button_status

class Button_line_admin(admin.ModelAdmin):
    inlines=[
        Button_line
    ]

# class NoticeAdminForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = models.Notice

# class NoticeAdmin(admin.ModelAdmin):
#     form = NoticeAdminForm

# admin.site.register(models.Notice, NoticeAdmin)
admin.site.register(models.Button_con, Button_line_admin)
admin.site.register(models.Cal_table, Cal_data_table)
admin.site.register(models.Marketer_user, M_userAdmin)
admin.site.register(models.Items, Item_list_admin)
admin.site.register(models.Perform_data, Perform_list_admin)