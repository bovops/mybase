__author__ = 'ink08'
from django.contrib import admin
from models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name', 'descr',)
    list_filter = ('status',)
    ordering = ('name',)

admin.site.register(Client, ClientAdmin)