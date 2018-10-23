# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.template.defaultfilters import slugify
import datetime	

# Create your models here.
class Category(models.Model):
	name_max_length = 128
	name = models.CharField(max_length=name_max_length, unique=True)
	slug = models.SlugField(unique=True)
	created = models.DateTimeField(blank=True, auto_now_add = True)
	tooltip = models.CharField(max_length=name_max_length)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self): # For Python 2, use __unicode__ too
		return self.name

	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.name

class Workflow(models.Model):
	name_max_length = 128
	description_max_length = 512
	keywords_max_length = 256
	name = models.CharField(max_length=name_max_length, unique=True)
	slug = models.SlugField(unique=True)
	description = models.CharField(max_length=description_max_length, default='')
	views = models.IntegerField(default=0)
	downloads = models.IntegerField(default=0)
	versionInit = models.CharField(max_length=name_max_length)
	category = models.ManyToManyField(Category)
	client_ip = models.GenericIPAddressField()
	keywords = models.CharField(max_length=keywords_max_length)
	json = JSONField()
	created = models.DateTimeField(blank=True, auto_now_add = True)
	
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self): # For Python 2, use __unicode__ too
		return self.name

	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.name