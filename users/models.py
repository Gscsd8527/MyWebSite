from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class UserInfo(AbstractUser):
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
#     is_delete = models.BooleanField(default=False, verbose_name='删除标记')
#
#     class Meta:
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name

class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱账号')
    is_superuser = models.BooleanField(default=False, verbose_name='是否是超级管理员')
    is_active = models.BooleanField(default=False, verbose_name='是否激活')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name