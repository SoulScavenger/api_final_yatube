# Generated by Django 3.2.16 on 2024-11-13 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0035_auto_20241113_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='auth.user', verbose_name='Подписчик'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='follow',
            name='following',
        ),
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='auth.user', verbose_name='Подписан на'),
            preserve_default=False,
        ),
    ]
