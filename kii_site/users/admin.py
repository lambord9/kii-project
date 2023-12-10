from django.contrib import admin

from .models import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','department', 'account_image']
    list_per_page = 30
    list_filter = ['user','department', 'account_image']

# Register your models here.
