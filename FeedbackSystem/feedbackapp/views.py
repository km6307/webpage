from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect, render


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
	     