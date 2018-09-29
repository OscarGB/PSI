# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our live easier.
	# Note that the first parameter os the template we wish to use.
	return render(request, 'rango/index.html', context=context_dict)
	return HttpResponse("<p>Rango says hey there partner!</p><a href='/rango/about/'>About page</a>")

def about(request):
	return HttpResponse("<p>Rango says here is the about page.</p><a href='/rango/'>Index page</a>")
