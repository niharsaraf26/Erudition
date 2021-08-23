from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Detail(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='user.png',blank=True, null=True)
    student_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=15)
    fname = models.CharField(max_length=15,default='')
    lname = models.CharField(max_length=15,default='')
    grade = models.IntegerField(default='0')
    email = models.EmailField(max_length=40,blank=True,default='ab@gmail.com')

    def __str__(self):
        return self.username


