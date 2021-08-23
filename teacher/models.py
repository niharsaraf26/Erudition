from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.




class Teacher_Detail(models.Model):
    user = models.OneToOneField(User,null=True, on_delete = models.CASCADE)
    username = models.CharField(max_length=100,blank=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Upload_video(models.Model):
    detail = models.ForeignKey( Teacher_Detail, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    grade = models.IntegerField(blank=True)
    video = models.FileField(upload_to='video')

    def __str__(self):
        return self.topic

class videoComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Upload_video, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',null=True,on_delete=models.CASCADE )
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + '...' + ' by ' + self.user.username

class Upload_file(models.Model):
    detail = models.ForeignKey(Teacher_Detail, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    grade = models.IntegerField(blank=True)
    video = models.FileField(upload_to='files')

    def __str__(self):
        return self.topic

class chat(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + '...' + ' by ' + self.user.username