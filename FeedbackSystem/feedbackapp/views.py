from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
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
    return render(request, 'login.html')


def admin(request):
   feedbackValues = Feedback.objects.all()
   return render(request, 'admin.html', {'feedbackValues': feedbackValues})


def submit(request):
    if request.method == 'POST':
        try:
            Feedback.objects.create(
                student=request.user,
                academicyear=request.POST.get('academicYear'),
                subject=request.POST.get('subject'),
                faculty_name=request.POST.get('facultyName'),
                course=request.POST.get('course'),
                semester=int(request.POST.get('semester')),
                feedback_date=request.POST.get('feedbackDate'),
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
            return redirect('feedback_form')
        except (ValueError, TypeError):
            messages.error(request, 'Please fill in all feedback fields correctly.')
    return render(request, '360°Feedback.html')
          