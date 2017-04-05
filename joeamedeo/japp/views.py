from django.shortcuts import render



def homeView(request):

	template = "japp/home.html"
	context = {
	}
	return render(request,template,context)

