from django.urls import path,include
from . import views

urlpatterns = [

    path("logout", views.logout_request, name="logout"),
    path('',views.student, name = 'student'),
    path('homepage.html',views.student, name = 'student'),
    path('contact.html', views.contact, name = 'student-contact'),
    path('grade1.html', views.grade1, name = 'grade1'),
    path('grade1sm.html', views.grade1sm, name='grade1sm'),
    path('grade2sm.html', views.grade2sm, name='grade2sm'),
    path('grade3sm.html', views.grade3sm, name='grade3sm'),
    path('grade4sm.html', views.grade4sm, name='grade4sm'),
    path('grade5sm.html', views.grade5sm, name='grade5sm'),
    path('grade2.html', views.grade2, name='grade2'),
    path('grade3.html', views.grade3, name='grade3'),
    path('grade4.html', views.grade4, name='grade4'),
    path('grade5.html', views.grade5, name='grade5'),
    path('about.html',views.about, name ='about'),
    path('signup.html',views.logout_request, name ='logout'),
    path('abc.html',views.abc, name ='abc'),
    path('video1.html',views.video1, name ='video1'),
    path('video2.html',views.video2, name ='video2'),
    path('video3.html',views.video3, name ='video3'),
    path('video4.html',views.video4, name ='video4'),
    path('video5.html',views.video5, name ='video5'),
    path('show/<str:pk>',views.showFile,name="showFile"),
    path('scomment/<str:pk>',views.scomment,name='scomment'),
    #path('profile.html',views.profile, name = 'profile'),
    path('schat/<str:pk>',views.schat,name='schat'),
    path('sprofile.html',views.sprofile,name='sprofile')

]