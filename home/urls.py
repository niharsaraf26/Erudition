from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [

    path('', views.home , name = 'home'),
    path('signup',views.handleSignup, name = 'handelsignup'),
    path('login',views.handleLogin, name = 'handelelogin'),
    path('logout',views.handleLogout, name = 'handelelogout'),
    path('reset_password', auth_views.PasswordResetView.as_view(),name='reset_password'),
path('reset_password_sent', auth_views.PasswordResetDoneView.as_view() , name='password_reset_done'),
path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

admin.site.site_header = "ERUDITION Admin"
admin.site.site_title = "ERUDITION Admin Portal"
admin.site.index_title = "Welcome to ERUDITION PORTAL"

