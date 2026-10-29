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
 

from django.contrib import messages
from django.shortcuts import redirect
from .models import Feedback


def submit(request):
    if request.method != 'POST':
        return redirect('home')

    if not request.user.is_authenticated:
        messages.error(request, 'Please login first.')
        return redirect('login')

    try:
        names = ['q1', 'q2', 'q3a', 'q3b',
                 'q3c', 'q4', 'q5', 'q6']

        ratings = []

        for name in names:
            value = request.POST.get(name)

            if not value:
                raise ValueError(f'{name} ki rating select nahi hui.')

            ratings.append(float(value))

        average = sum(ratings) / len(ratings)

        Feedback.objects.create(
            student=request.user,
            academicYear=request.POST.get('academicYear'),
            subject=request.POST.get('subject'),
            facultyName=request.POST.get('facultyName'),
            course=request.POST.get('course'),
            semester=request.POST.get('semester'),
            feedbackDate=request.POST.get('feedbackDate') or None,
            rating=average
        )

        messages.success(request, 'Feedback saved successfully!')

    except Exception as e:
        print("FEEDBACK SAVE ERROR:", repr(e))
        messages.error(request, f'Feedback save failed: {e}')

    return redirect('home')