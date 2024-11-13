# Generated by Django 3.2.16 on 2024-11-13 16:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0034_alter_follow_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='following',
        ),
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
