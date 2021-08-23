from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.apps import apps
from django.forms import forms
from .forms import Edit


Upload_file=apps.get_model('teacher', 'Upload_file')
Teacher = apps.get_model('teacher', 'Teacher_Detail')
videoComment = apps.get_model('teacher', 'videoComment')
Detail_student = apps.get_model('home', 'Detail')
Upload = apps.get_model('teacher','Upload_video')
chat = apps.get_model('teacher', 'chat')

# Create your views here.
@login_required(login_url='home')
def student(request):
    name = Detail_student.objects.get(user=request.user)
    form = Edit()
    if request.method == 'POST':
        form = Edit(request.POST, request.FILES, instance=name)
        if form.is_valid():
            form.save()

    inputId = request.user
    detail = Detail_student.objects.get(username = inputId)
    print(detail)
    context = {'c': detail,'form':form }
    return render(request, 'student/homepage.html',context)


def abc(request):
    return (request, 'student/abc.html')

@login_required(login_url='home')
def contact(request):
    inputId = request.user
    detail = Detail_student.objects.get(username=inputId)
    print(detail)
    context = {'c': detail}
    return render(request, 'student/contact.html',context)

@login_required(login_url='home')
def grade1(request):
    detail = Upload.objects.filter(grade = '1')
    context = {'videos':detail}
    return render(request, 'student/grade1.html',context)

@login_required(login_url='home')
def grade2(request):
    detail = Upload.objects.filter(grade='2')
    context = {'videos': detail}

    return render(request, 'student/grade2.html',context)

@login_required(login_url='home')
def grade3(request):
    detail = Upload.objects.filter(grade='3')
    inputId = request.user
    detail1 = Detail_student.objects.get(username=inputId)
    print(detail)
    context = {'videos': detail,'c':detail1}
    return render(request, 'student/grade3.html',context)

@login_required(login_url='home')
def grade4(request):
    detail = Upload.objects.filter(grade='4')
    context = {'videos': detail}
    return render(request, 'student/grade4.html',context)

@login_required(login_url='home')
def grade5(request):
    detail = Upload.objects.filter(grade='5')
    context = {'videos': detail}
    return render(request, 'student/grade5.html',context)

@login_required(login_url='home')
def grade1sm(request):
    videos = Upload_file.objects.filter(grade='1')
    context = {"videos": videos}

    return render(request, 'student/grade1sm.html',context)

@login_required(login_url='home')
def grade2sm(request):
    videos = Upload_file.objects.filter(grade='2')
    context = {"videos": videos}

    return render(request, 'student/grade2sm.html', context)

@login_required(login_url='home')
def grade3sm(request):
    videos = Upload_file.objects.filter(grade='3')
    context = {"videos": videos}

    return render(request, 'student/grade3sm.html', context)

@login_required(login_url='home')
def grade4sm(request):
    videos = Upload_file.objects.filter(grade='4')
    context = {"videos": videos}

    return render(request, 'student/grade4sm.html', context)

@login_required(login_url='home')
def grade5sm(request):
    videos = Upload_file.objects.filter(grade='5')
    context = {"videos": videos}

    return render(request, 'student/grade5sm.html',context)

@login_required(login_url='home')
def video1(request):
    detail = Upload.objects.filter(grade='1')
    print(detail)
    context = {'videos': detail}

    return render(request, 'student/video1.html',context)

@login_required(login_url='home')
def video2(request):
    detail = Upload.objects.filter(grade='2')
    print(detail)
    context = {'videos': detail}
    return render(request, 'student/video2.html',context)

@login_required(login_url='home')
def video3(request):
    detail = Upload.objects.filter(grade='3')
    print(detail)
    context = {'videos': detail}
    return render(request, 'student/video3.html',context)

@login_required(login_url='home')
def video4(request):
    detail = Upload.objects.filter(grade='4')
    print(detail)
    context = {'videos': detail}
    return render(request, 'student/video4.html',context)

@login_required(login_url='home')
def video5(request):
    detail = Upload.objects.filter(grade='5')
    print(detail)
    context = {'videos': detail}
    return render(request, 'student/video5.html',context)

@login_required(login_url='home')
def about(request):
    inputId=request.user
    detail = Detail_student.objects.get(username=inputId)
    print(detail)
    context = {'c': detail}
    return render(request, 'student/about.html',context)


def logout_request(request):
    logout(request)
    messages.info(request, "LOGOUT SUCCESSFULLY")
    return redirect("home")

def scomment(request,pk):
    news = pk
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postsno')
        parentsno = request.POST.get('parentsno')
        print(parentsno)
        post = Upload.objects.get(id=pk)
        if parentsno == '':
            comment = videoComment(comment=comment, user=user, post=post)
            comment.save()
        else:
            parent = videoComment.objects.get(sno=parentsno)
            comment = videoComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
    video = Upload.objects.get(id=pk)
    comment = videoComment.objects.filter(post=video, parent=None)
    replies = videoComment.objects.filter(post=video).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    return render(request, 'student/scomment.html', {'comments': comment, 'id': news, 'replyDict': replyDict})
@login_required(login_url='home')
def showFile(request,pk):
    return (render,'student/show.html')

def schat(request,pk):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        comment = chat(comment=comment,user=user)
        comment.save()
    comment1 = chat.objects.all()

    return render(request,'student/schat.html',{'comments_c': comment1})

def sprofile(request):
    name = Detail_student.objects.get(user=request.user)
    form = Edit()
    if request.method == 'POST':
        form = Edit(request.POST, request.FILES, instance=name)
        if form.is_valid():
            form.save()

    inputId = request.user
    detail = Detail_student.objects.get(username=inputId)
    print(detail)
    context = {'c': detail, 'form': form}

    return render(request,'student/sprofile.html',context)