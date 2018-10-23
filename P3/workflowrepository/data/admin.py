# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from data.models import Category, Workflow

class CateegoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",)}
	list_display = ['name', 'slug']

class WorkflowAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'views', 'downloads', 'client_ip', 'created']
	pass

admin.site.register(Category, CateegoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)

# Register your models here.
