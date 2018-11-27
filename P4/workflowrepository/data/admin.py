# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from data.models import Category, Workflow

class CategoryAdmin(admin.ModelAdmin):
	# prepopulated_fields = {'slug':('name',)}
	list_display = ['name', 'slug']
	fields = ['name', 'tooltip']
	# readonly_fields = ['slug']

class WorkflowAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'views', 'downloads', 'client_ip', 'created']
	fields = ['name', 'description', 'versionInit', 'category', 'client_ip', 'keywords', 'json']
	# readonly_fields = ['slug']
	pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)

# Register your models here.
