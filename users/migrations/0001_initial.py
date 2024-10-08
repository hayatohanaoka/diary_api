# Generated by Django 5.1 on 2024-08-22 13:32

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(help_text='20字以内かつ、使用可能記号は「@/./+/-/_」のみ', max_length=20, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='ユーザー名')),
                ('email', models.EmailField(blank=True, error_messages={'unique': 'このユーザー名は既に使用されています。'}, max_length=254, verbose_name='メールアドレス')),
                ('nickname', models.CharField(blank=True, max_length=20, verbose_name='ニックネーム')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='管理者')),
                ('is_active', models.BooleanField(default=True, verbose_name='使用中フラグ')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='追加日')),
            ],
            options={
                'verbose_name': 'ユーザー',
                'verbose_name_plural': 'ユーザー管理',
                'db_table': 'tbl_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
