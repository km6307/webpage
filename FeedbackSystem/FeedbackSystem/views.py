from django.shortcuts import render


def home(request):
	return render(request, '360°Feedback.html')
def login(request):
	return render(request,'login.html')   