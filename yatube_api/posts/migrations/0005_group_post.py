# Generated by Django 3.2.16 on 2024-11-12 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20241112_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='posts.post'),
            preserve_default=False,
        ),
    ]