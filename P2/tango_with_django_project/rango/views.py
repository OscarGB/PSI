# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("<p>Rango says hey there partner!</p><a href='/rango/about/'>About page</a>")

def about(request):
	return HttpResponse("<p>Rango says here is the about page.</p><a href='/rango/'>Index page</a>")
