from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from app1.form import RegisterForm
# Create your views here.
def login(request):
    return render(request,'userlogin.html')

def reg(request):
    return render(request,'RegisterPage.html')

def register(request):
        if request.method=='POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            # if password1 == password2:
            user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password1  # Use 'password' instead of 'password1'
                )
            user.save()
            print('user created')
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
       
