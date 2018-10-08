# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page


def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	category_list = Category.objects.order_by('-likes')[:5]
	pages_list = Page.objects.order_by('-views')[:5]
	context_dict = {"categories": category_list, "pages": pages_list}
	# context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our live easier.
	# Note that the first parameter os the template we wish to use.
	return render(request, 'rango/index.html', context=context_dict)
	# return HttpResponse("<p>Rango says hey there partner!</p><a href='/rango/about/'>About page</a>")

def show_category(request, category_name_slug):
	# Create a context dictionary which we can pass
	# to the template rendering engine.
	context_dict = {}
	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		category = Category.objects.get(slug=category_name_slug)

		# Retrieve all of the associated pages.
		# Note that filter() will return a list of page objects or an empty list
		pages = Page.objects.filter(category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages

		# We also add the category object from
		# the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category

	except Category.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything -
		# the template will display the "no category" message for us.
		context_dict['category'] = None
		context_dict['pages'] = None

	# Go render the response and return it to the client.
	return render(request, 'rango/category.html', context_dict)

def about(request):
	return render(request, 'rango/about.html')
