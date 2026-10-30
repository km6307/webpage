from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
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

    if not request.user.is_authenticated:
        messages.error(request, 'Please login first.')
        return redirect('login')

    ratings = [
        int(request.POST.get('q1', 0)),
        int(request.POST.get('q2', 0)),
        int(request.POST.get('q3a', 0)),
        int(request.POST.get('q3b', 0)),
        int(request.POST.get('q3c', 0)),
        int(request.POST.get('q4', 0)),
        int(request.POST.get('q5', 0)),
        int(request.POST.get('q6', 0)),
    ]
    average_rating = sum(ratings) / len(ratings)

    Feedback.objects.create(
        student=request.user,
        academicYear=request.POST.get('academicYear'),
        subject=request.POST.get('subject'),
        facultyName=request.POST.get('facultyName'),
        course=request.POST.get('course'),
        semester=request.POST.get('semester'),
        feedbackDate=request.POST.get('feedbackDate') or None,
        rating=average_rating,
    )
    messages.success(request, 'Feedback saved successfully!')
    return redirect('login')