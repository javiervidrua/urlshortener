from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from shortener.models import Url

import uuid

# Create your views here.
# https://programmerah.com/forbidden-403-csrf-verification-failed-request-aborted-django-4435/
#@require_http_methods(['GET', 'POST', 'DELETE', 'PUT'])
#@csrf_exempt # This has to be here so the client is able to do a POST request
def index(request):
	url = None

	if request.method == 'GET':
		try:
			url = request.GET['id']
		except:
			url = None
		return shortened_url_create(url)

#	elif request.method == 'POST':
#		try:
#			url = request.POST['id']
#		except:
#			url = None
#		return shortened_url_create(url)
#
#	elif request.method == 'PUT':
#		try:
#			url = request.POST['id']
#		except:
#			url = None
#		return shortened_url_update(url)
#
#	elif request.method == 'DELETE':
#		try:
#			url = request.POST['id']
#		except:
#			url = None
#		return shortened_url_delete(url)

	else:
		return HttpResponse("Error: Bad request")

def shortened_url_create(url):
	if url == None:
		return HttpResponse("Error: Invalid URL")

	try:
		id = shortened_url_get(url)
		if id == None:
			id = uuid.uuid4()
			new_url = Url(short_url=id, long_url=url)
			new_url.save()
			return HttpResponse("https://javiervidrua.pythonanywhere.com/?id=" + str(id))
		else:
			return HttpResponse("https://javiervidrua.pythonanywhere.com/?id=" + str(id))
	except:
		return HttpResponse("Error: System error")

def shortened_url_get(url):
    if url == None:
        return None

    try:
        id = Url.objects.get(long_url=url).short_url
        return id
    except:
        return None
