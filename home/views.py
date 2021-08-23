from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,get_user
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
#from .decorators import admin_only
from django.contrib.auth.models import Group
from django.apps import apps
Teacher = apps.get_model('teacher', 'Teacher_Detail')

from .models import Detail




from .models import Detail
grade = ""
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        grade = request.POST['grade']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if not username.isalnum():
            messages.error(request, 'username should only contain lettrs and numbers')
            return redirect('home')
        if len(username) > 10:
            messages.error(request, 'username is very long')
            return redirect('home')
        if len(pass1) < 8:
            messages.error(request, 'password atleast contain 8 characters')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "password do not match")
            return redirect('home')

        a = Detail.objects.all()
        for b in a:
            if username == b.username or email == b.email:
                messages.error(request, 'username already taken')
                return redirect('home')
            if  email == b.email:
                messages.error(request, 'email already taken')
                return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        detail = Detail(username=username, grade=grade, fname=fname, lname=lname,email=email)
        detail.save()

        email_subject= 'ERUDITION TEAM'
        email_body = 'Your account has been successfully registered to our website.We hope you will like our website'
        send_mail(
                email_subject,
                email_body,
              "testuser@gmail.com",
              [email],
        )
        messages.success(request,'your account has been successfully created')
        return redirect('home')
    else:
        return HttpResponse("not allowed")
@csrf_exempt
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            c = Detail.objects.get(username=loginusername)
            messages.success(request, ' successfully logged in')
            try:
                d = Teacher.objects.get(username=loginusername)
            except Teacher.DoesNotExist:
                d = None
            if d is not None:
                e = Detail.objects.get(username=request.user)
                return render(request, 'teacher/homepagetr.html', {'d': d,'e':e})
            else:
                return render(request, 'student/homepage.html', {'c': c})
        else:
            messages.error(request, 'Invalid credentials : PLEASE TRY AGAIN')
            return redirect('home')
    else:
        return HttpResponse("404-error found")



def handleLogout(request):
    logout(request)
    messages.success(request,'LOG OUT SUCCESSFULLY')
    return redirect('home')

