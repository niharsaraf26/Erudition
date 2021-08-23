from django.contrib import admin
from .models import Upload_video, Teacher_Detail, videoComment, Upload_file, chat

# Register your models here.
admin.site.register(Upload_video)
admin.site.register(Teacher_Detail)
admin.site.register(videoComment)
admin.site.register(Upload_file)
admin.site.register(chat)