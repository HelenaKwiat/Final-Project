from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
# 	# template = loader.get_template('metric/index.html')
# 	context = {}
# 	# return HttpResponse(template.render(context, request))
# 	return render(request, 'metric/index.html', context)



def index(request):
    # self.model.objects.all().update(is_immortal=True)
	context = {'hello': 10}
	return render(request, 'metric/index.html', context)


def details(request):
	return HttpResponse("You're voting on question ")
# def set_mortal(request):
#     # self.model.objects.all().update(is_immortal=False)
#     self.message_user(request, "All heroes are now mortal")
#     return HttpResponseRedirect("../")
