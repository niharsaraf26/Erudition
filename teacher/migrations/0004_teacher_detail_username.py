# Generated by Django 3.1.1 on 2020-10-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacher_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_detail',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]