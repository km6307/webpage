from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
import traceback
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
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
    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'admin.html', {'feedbacks': feedbacks})


def submit(request):
    print(">>> SUBMIT CALLED", request.method, request.user)
    if request.method != 'POST':
        return redirect('home')

    if not request.user.is_authenticated:
        print(">>> USER LOGGED IN NAHI HAI")
        messages.error(request, 'Please login first.')
        return redirect('login')

    try:
        fields = ['q1', 'q2', 'q3a', 'q3b', 'q3c', 'q4', 'q5', 'q6']
        ratings = [int(request.POST.get(f) or 0) for f in fields]
        average_rating = sum(ratings) / len(ratings)

        obj = Feedback.objects.create(
            student=request.user,
            academicYear=request.POST.get('academicYear') or '',
            subject=request.POST.get('subject') or '',
            facultyName=request.POST.get('facultyName') or '',
            course=request.POST.get('course') or '',
            semester=request.POST.get('semester') or '',
            feedbackDate=request.POST.get('feedbackDate') or None,
            rating=average_rating,
        )
        print(">>> SAVED ID:", obj.id)
        messages.success(request, 'Feedback saved successfully!')
    except Exception as e:
        traceback.print_exc()
        messages.error(request, f'Error: {e}')

    return redirect('login')
def delete(request, feedback_id):
       feedback = get_object_or_404(Feedback, id=feedback_id)
       feedback.delete()
       return redirect("admin_panel")   