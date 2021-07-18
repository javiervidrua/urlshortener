from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from shortener.models import Url

# Create your views here.
def index(request):
	if request.method == 'GET':
		try:
			short_url = request.GET['id']
		except:
			short_url = None
		return shortened_url_get(short_url)

	else:
		return HttpResponse("Error: Bad request")

def shortened_url_get(url):
	if url == None:
		return HttpResponse("Error: Invalid URL")

	try:
		long_url = Url.objects.get(short_url=url).long_url
		return HttpResponseRedirect(str(long_url))
	except:
		return HttpResponse("Error: System error")
