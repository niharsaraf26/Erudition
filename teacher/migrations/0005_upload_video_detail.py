# Generated by Django 3.1.1 on 2020-10-28 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_teacher_detail_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_video',
            name='detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher_detail'),
        ),
    ]
