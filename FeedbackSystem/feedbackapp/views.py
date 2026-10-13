from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from .models import Feedback


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')

        messages.info(request, 'Either Username or Password is Incorrect')
        return render(request, 'login.html')
    return render(request, 'login.html')
		
def home(request):
    return render(request, '360°Feedback.html')

def logout(request):
    return render(request, 'login.html')
    messages.info(request,"feedback  send successfully.your are eligible for next feedback after 1 month.")

def submit(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    ratings = {}
    for name in ('teaching', 'communication', 'support', 'growth'):
        value = request.POST.get(name, '').strip()
        if not value:
            ratings[name] = None
            continue
        try:
            rating = int(value)
        except ValueError:
            messages.error(request, 'Ratings must be between 1 and 5.')
            return redirect('home')
        if not 1 <= rating <= 5:
            messages.error(request, 'Ratings must be between 1 and 5.')
            return redirect('home')
        ratings[name] = rating

    Feedback.objects.create(
        roleValue=request.POST.get('roleValue', '').strip(),
        teacher=request.POST.get('teacher', '').strip(),
        subject=request.POST.get('subject', '').strip(),
        target=request.POST.get('target', '').strip(),
        class_name=request.POST.get('class_name', '').strip(),
        year=request.POST.get('year', '').strip(),
        comment=request.POST.get('comment', '').strip(),
        **ratings,
    )
    messages.success(request, 'Feedback submitted successfully.')
    return redirect('home')
   
	     	    
