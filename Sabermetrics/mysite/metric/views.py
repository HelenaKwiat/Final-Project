from django.http import HttpResponse

def index(request):
	for i in range(10):
		x = i + 1
	return HttpResponse("Hello, World here's your metric.")
