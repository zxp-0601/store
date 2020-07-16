import datetime
import random

from django.db import models
# from tools.basemodels import BaseModels
from django.utils import timezone
# Create your models here.

def default_info():
    signs = ['天生我材必有用','我若成魔，天下无佛','为中华民族的伟大复兴而读书','业精于勤而荒于嬉，行成于思而毁于随','学而不思则罔，思而不学则殆']
    return random.choice(signs)

class User(models.Model):
    username = models.CharField('用户名',max_length=11)
    email = models.EmailField()
    password = models.CharField('密码',max_length=32)
    avatar = models.ImageField('头像',upload_to='avatar', null=True)
    phone = models.CharField('手机号',max_length=11, default='')
    is_active = models.BooleanField('是否活跃',default=True)
    gender = models.CharField('性别',max_length=10,default='')
    birthday = models.DateField(verbose_name='生日',default=datetime.date(1900,1, 1), null=True)
    info = models.CharField('简介',max_length=100,default=default_info)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        db_table = 'user'









