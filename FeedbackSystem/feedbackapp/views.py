from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect, render
from django.core.mail import send_mail


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

def submit(request):
    if request.method != 'POST':
        return redirect('home')

        roleValue = request.POST.get('roleValue') or request.POST.get('role', '')
        teacher = request.POST.get('teacher') or request.POST.get('Teacher', '')
        subject = request.POST.get('subject', '')
        target = request.POST.get('target', '')
        className = (
                request.POST.get('className')
                or request.POST.get('class_name')
                or request.POST.get('class', '')
            )
        year = request.POST.get('year', '')
        comment = request.POST.get('comment') or request.POST.get('comments', '')

        rating_names = ('teaching', 'communication', 'support', 'growth')
        ratings = {
                name: f'{int(request.POST[name]) * 20}%'
                for name in rating_names
                if request.POST.get(name, '').isdigit()
                and 1 <= int(request.POST[name]) <= 5
            }

        feedback = '\n'.join((
                f'Role: {roleValue or "Not provided"}',
                f'Teacher: {teacher or "Not provided"}',
                f'Subject: {subject or "Not provided"}',
                f'Feedback for: {target or "Not provided"}',
                f'Class: {className or "Not provided"}',
                f'Year: {year or "Not provided"}',
                'Ratings:',
                *(f'  {name.title()}: {value}' for name, value in ratings.items()),
                f'Comment: {comment or "Not provided"}',
            ))

        send_mail(
                'Feedback Was Submitted',
                feedback,
                'mppolytechnic',
                ['hod sir email','principle sir email'],
                fail_silently=False,
            )
        messages.info(request,"mail send successfully")
        return redirect('login')
    else:
       messages.info(request,"mail not send")
       return redirect('home')
   
	     	    