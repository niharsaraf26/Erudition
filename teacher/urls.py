from django.urls import path,include
from . import views

urlpatterns = [
    path('homepage.html' ,views.t_homepage, name='t_homepage'),
    path('abouttr.html', views.t_about , name = 't_about'),
    path('contacttr.html', views.t_contact, name='t_contact'),
    path('video.html', views.t_video,name = 't_video'),
    path('grade1sm.html', views.t_grade1sm, name='t_grade1sm'),
    path('grade2sm.html', views.t_grade2sm, name='t_grade2sm'),
    path('grade3sm.html', views.t_grade3sm, name='t_grade3sm'),
    path('grade4sm.html', views.t_grade4sm, name='t_grade4sm'),
    path('grade5sm.html', views.t_grade5sm, name='t_grade5sm'),
    path('grade1tr.html', views.t_grade1, name='t_grade1'),
    path('grade2tr.html', views.t_grade2, name='t_grade2'),
    path('grade3tr.html', views.t_grade3, name='t_grade3'),
    path('grade4tr.html', views.t_grade4, name='t_grade4'),
    path('grade5tr.html', views.t_grade5, name='t_grade5'),
    path('videotr1.html',views.t_video1,name='t_video1'),
    path('videotr2.html', views.t_video2, name='t_video2'),
    path('videotr3.html', views.t_video3, name='t_video3'),
    path('videotr4.html', views.t_video4, name='t_video4'),
    path('videotr5.html', views.t_video5, name='t_video5'),
    path('comment/<str:pk>',views.handleComment, name = 'handleComment'),
    path('chat/<str:pk1>',views.handlechat, name = 'handlechat'),
    path('file.html',views.handleFile,name = 'handleFile'),
    path('tprofile.html',views.tprofile,name='tprofile')

]