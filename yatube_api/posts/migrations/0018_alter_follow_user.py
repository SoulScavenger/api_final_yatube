# Generated by Django 3.2.16 on 2024-11-13 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20241113_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]
