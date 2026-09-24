from django.shortcuts import render


def home(request):
	return render(request, '360°Feedback.html')
def Registration(request):
	return render(request,'Registration.html')
def login(request):
	return render(request,'login.html')   