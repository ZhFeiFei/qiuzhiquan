# Generated by Django 2.0.1 on 2018-01-20 07:09

import DjangoUeditor.models
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m', verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('desc', models.TextField(verbose_name='简介')),
                ('profession', models.CharField(max_length=50, verbose_name='专业')),
                ('year', models.CharField(choices=[('1', '2018届'), ('2', '2017届'), ('3', '2016届'), ('4', '2015届')], max_length=50, verbose_name='年级')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100, verbose_name='评论')),
                ('pub_time', models.DateTimeField(default=datetime.datetime(2018, 1, 20, 15, 9, 15, 101072), verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=100, verbose_name='问题')),
                ('answer', models.TextField(default='', max_length=500, verbose_name='回答')),
                ('image', models.ImageField(blank=True, null=True, upload_to='faq/%Y/%m', verbose_name='问答图片')),
            ],
            options={
                'verbose_name': '问答',
                'verbose_name_plural': '问答',
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('image', models.ImageField(upload_to='interview/%Y/%m', verbose_name='封面')),
                ('company', models.CharField(max_length=50, verbose_name='公司')),
                ('trade', models.CharField(choices=[('t1', '互联网'), ('t2', '网络安全'), ('t3', '运营商'), ('t4', '银行'), ('t5', '集成商'), ('t6', '国企'), ('t7', '云计算'), ('t8', '其他')], default='t1', max_length=10, verbose_name='行业')),
                ('location', models.CharField(choices=[('l1', '北京'), ('l2', '上海'), ('l3', '广州'), ('l4', '深圳'), ('l5', '全国'), ('l6', '其他')], default='l1', max_length=10, verbose_name='地区')),
                ('pub_time', models.DateTimeField(default=datetime.datetime(2018, 1, 20, 15, 9, 15, 100088), verbose_name='发布时间')),
                ('read_counts', models.IntegerField(default=0, verbose_name='阅读次数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Author', verbose_name='所属作者')),
            ],
            options={
                'verbose_name': '面经',
                'verbose_name_plural': '面经',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='interview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Interview', verbose_name='文章外键'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户外键'),
        ),
    ]