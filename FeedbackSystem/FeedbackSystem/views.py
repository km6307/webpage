from django.shortcuts import render


def home(request):
	return render(request, '360°Feedback.html')
def Registration(request):      
      if request.method == 'POST':
            Name = request.POST['first_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            # print(first_name,last_name,username,email,password,cpassword)
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already Exist")
                    return render(request, 'register.html')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "email already Exist")
                    return render(request, 'registration.html')
                else:
                    user = User.objects.create_user(Name=Name, username=username,
                                                    email=email, password=password)
                    user.save()
                    messages.info(request, "User Created Successfully")
                    # return redirect("/")  #for home page
                    return render(request, 'registration.html')
            else:
                messages.info(request, "Password and Confirm Password Do not Match")
                return render(request, 'registration.html')
      else:
         return render(request, 'registration.html')
     
	   
def login(request):
	return render(request,'login.html')   