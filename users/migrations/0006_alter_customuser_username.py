# Generated by Django 5.1 on 2024-08-22 16:11

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text='20字以内かつ、使用可能記号は「@/./+/-/_」のみ', max_length=20, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='ユーザー名'),
        ),
    ]
