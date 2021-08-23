from django.shortcuts import render
from .models import Upload_video, videoComment, Upload_file, chat
from django.contrib.auth.decorators import login_required
from .forms import Video_form, Upload_form, Edit
from django.apps import apps
Teacher = apps.get_model('teacher', 'Teacher_Detail')
Detail = apps.get_model('home', 'Detail')
from .templatetags import extras


# Create your views here.
@login_required(login_url='home')
def t_homepage(request):
    name = Detail.objects.get(user=request.user)
    form = Edit()

    if request.method == 'POST':
        form = Edit(request.POST, request.FILES,instance=name)
        if form.is_valid():
            form.save()
    inputid = request.user
    try:
        detail = Teacher.objects.get(username = inputid)
    except Teacher.DoesNotExist:
        detail = None
    e = Detail.objects.get(username=inputid)
    context = {'d': detail, 'forms': form,'e':e}
    return render(request, 'teacher/homepagetr.html', context)

@login_required(login_url='home')
def t_about(request):
    return render(request, 'teacher/abouttr.html')

@login_required(login_url='home')
def t_contact(request):
    return render(request,'teacher/contacttr.html')

@login_required(login_url='home')
def t_grade1sm(request):
    videos = Upload_file.objects.filter(grade='1')
    context = {"videos": videos}
    return render(request,'teacher/grade1smtr.html',context)

@login_required(login_url='home')
def t_grade2sm(request):
    videos = Upload_file.objects.filter(grade='2')
    context = {"videos": videos}
    return render(request,'teacher/grade2smtr.html',context)

@login_required(login_url='home')
def t_grade3sm(request):
    videos = Upload_file.objects.filter(grade='3')
    context = {"videos": videos}
    return render(request,'teacher/grade3smtr.html',context)

@login_required(login_url='home')
def t_grade4sm(request):
    videos = Upload_file.objects.filter(grade='4')
    context = {"videos": videos}
    return render(request,'teacher/grade4smtr.html',context)

@login_required(login_url='home')
def t_grade5sm(request):
    videos = Upload_file.objects.filter(grade='5')
    context = {"videos": videos}
    return render(request,'teacher/grade5smtr.html',context)

@login_required(login_url='home')
def t_grade1(request):
    return render(request,'teacher/grade1tr.html')

@login_required(login_url='home')
def t_grade2(request):
    return render(request,'teacher/grade2tr.html')

@login_required(login_url='home')
def t_grade3(request):
    return render(request,'teacher/grade3tr.html')

@login_required(login_url='home')
def t_grade4(request):
    return render(request,'teacher/grade4tr.html')

@login_required(login_url='home')
def t_grade5(request):
    return render(request,'teacher/grade5tr.html')

@login_required(login_url='home')
def t_video(request):

    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postsno')
        try:
            post =  Upload_video.objects.get(id=postSno)
        except Upload_video.DoesNotExist:
            post = None
            if post is not None:
                comment = videoComment(comment=comment,user=user,post=post)
                comment.save()

    form = Video_form
    form = Video_form(data=request.POST or None)

    if request.method == 'POST':
        form = Video_form(data=request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()

    if request.method == 'POST':
        d = request.POST.get('abcd')
        try:
            video = Upload_video.objects.get(id=d)
        except Upload_video.DoesNotExist:
            video = None
        if video is not None:
            video.delete()


    videos = Upload_video.objects.filter(detail__username=request.user)
    context = {"forms": form, "videos": videos}
    return render(request, 'teacher/video.html', context)

@login_required(login_url='home')
def t_video1(request):
    videos = Upload_video.objects.filter(grade = '1')
    context = {"videos": videos}
    return render(request, 'teacher/videotr1.html', context)

@login_required(login_url='home')
def t_video2(request):
    videos = Upload_video.objects.filter(grade='2')
    context = {"videos": videos}
    return render(request,'teacher/videotr2.html',context)

@login_required(login_url='home')
def t_video3(request):
    videos = Upload_video.objects.filter(grade='3')
    context = {"videos": videos}
    return render(request,'teacher/videotr3.html',context)

@login_required(login_url='home')
def t_video4(request):
    videos = Upload_video.objects.filter(grade='4')
    context = {"videos": videos}
    return render(request,'teacher/videotr4.html',context)

@login_required(login_url='home')
def t_video5(request):
    videos = Upload_video.objects.filter(grade='5')
    context = {"videos": videos}
    return render(request,'teacher/videotr5.html',context)

@login_required(login_url='home')
def handleComment(request,pk):
    news = pk
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postsno')
        parentsno = request.POST.get('parentsno')
        print(parentsno)
        post =  Upload_video.objects.get(id=pk)
        if parentsno == '':
            comment = videoComment(comment=comment,user=user,post=post)
            comment.save()
        else:
            parent = videoComment.objects.get(sno=parentsno)
            comment = videoComment(comment=comment, user=user, post=post,parent=parent)
            comment.save()
    video = Upload_video.objects.get(id=pk)
    comment = videoComment.objects.filter(post = video,parent = None)
    replies = videoComment.objects.filter(post = video).exclude(parent=None)
    replyDict= {}
    for reply in replies:
        if reply.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    return render(request, 'teacher/comment.html', {'comments': comment, 'id':news, 'replyDict': replyDict})

@login_required(login_url='home')
def handleFile(request):
    form1 = Upload_form
    form1 = Upload_form(data=request.POST or None)
    if request.method == 'POST':
        form1 = Upload_form(data=request.POST or None, files=request.FILES)
        print(form1)
        if form1.is_valid():
            form1.save()
    videos = Upload_file.objects.filter(detail__username=request.user)

    if request.method == 'POST':
        d = request.POST.get('abcd')

        try:
            video = Upload_video.objects.get(id=d)
            print(video)
        except Upload_video.DoesNotExist:
            video = None
        if video is not None:
            video.delete()

    context1 = {'forms': form1,"videos":videos}
    return render(request, 'teacher/file.html', context1)

def handlechat(request,pk1):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        comment = chat(comment=comment,user=user)
        comment.save()
    comment1 = chat.objects.all()
    return render(request, 'teacher/chat.html', {'comments_c': comment1})

def tprofile(request):
    name = Detail.objects.get(user=request.user)
    form = Edit()

    if request.method == 'POST':
        form = Edit(request.POST, request.FILES, instance=name)
        if form.is_valid():
            form.save()
    inputid = request.user
    try:
        detail = Teacher.objects.get(username=inputid)
    except Teacher.DoesNotExist:
        detail = None
    e = Detail.objects.get(username=inputid)
    context = {'d': detail, 'forms': form, 'e': e}
    return render(request ,'teacher/tprofile.html',context)