# Generated by Django 3.1.1 on 2020-10-25 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload_video',
            old_name='title',
            new_name='topic',
        ),
    ]
