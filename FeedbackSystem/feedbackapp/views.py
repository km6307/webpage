from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from .models import Feedback


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')
        role = request.POST.get('role', '').strip().lower()
        user = authenticate(request, username=username, password=password)

        if user is not None and (role != 'admin' or user.is_staff or user.is_superuser):
            auth_login(request, user)

            if user.is_staff or user.is_superuser:
                return redirect('admin')
            return redirect('home')

        messages.info(request, 'Either Username or Password is Incorrect')
        return render(request, 'login.html')

    return render(request, 'login.html')


def home(request):
    return render(request, '360°Feedback.html')


def logout(request):
     auth_logout(request)
     return redirect('login')


def admin(request):
    return render(request, 'admin.html')
 

def submit(request):
    if request.method != 'POST':
        return redirect('home')

    try:
        if not request.user.is_authenticated:
            messages.error(request, 'Please login first.')
            return redirect('login')

        Feedback.objects.create(
            student=request.user,
            academicyear=request.POST.get('academicYear'),
            semester=request.POST.get('semester'),
            subject=request.POST.get('subject'),
            faculty=request.POST.get('facultyName'),
            course=request.POST.get('course'),
            feedback_date=request.POST.get('feedbackDate') or None,
            q1=int(request.POST.get('q1')),
            q2=int(request.POST.get('q2')),
            q3a=int(request.POST.get('q3a')),
            q3b=int(request.POST.get('q3b')),
            q3c=int(request.POST.get('q3c')),
            q4=int(request.POST.get('q4')),
            q5=int(request.POST.get('q5')),
            q6=int(request.POST.get('q6')),
        )

        messages.success(request, 'Feedback saved successfully!')

    except Exception as e:
        print("FEEDBACK SAVE ERROR:", repr(e))
        messages.error(request, f'Feedback save failed: {e}')

    return redirect('home')
