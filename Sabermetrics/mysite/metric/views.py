from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# template = loader.get_template('metric/index.html')
	context = {}
	# return HttpResponse(template.render(context, request))
	return render(request, 'metric/index.html', context)
