# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rango.models import Category, Page

class CateegoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",)}

class PageAdmin(admin.ModelAdmin):
	list_display = ['title','category', 'url']
	pass

admin.site.register(Category, CateegoryAdmin)
admin.site.register(Page, PageAdmin)


# Register your models here.
