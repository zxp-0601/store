"""
一些工具函数，在其他模块可被调用
"""
import time
from hashlib import md5
import jwt
from django.conf import settings
from django.core import mail
import random

from django.http import JsonResponse

from user.models import User


def data_md5(data):
    """对数据进行MD5加密"""
    m = md5()
    m.update(data.encode())
    return m.hexdigest()

def make_token(username,expire=3600*24):
    """生成token"""
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username':username,'exp':now+expire}
    return jwt.encode(payload,key)

def make_code():
    """生成四位随机验证码，包含数字字母"""
    code = ""
    for i in range(4):
        ran1 = random.randint(0, 9)
        ran2 = chr(random.randint(65, 90))
        add = random.choice([ran1, ran2])
        code = "".join([code, str(add)])
    return code

def send_email(email,code):
    """发送邮件"""
    mail.send_mail(
        '用于注册的验证码，一分钟有效',
        code,
        '577603561@qq.com',
        recipient_list=[email],
    )
    print('邮件已经发送')

def logging_check(func):
    """校验登录"""
    def wrap(request,*args,**kwargs):
        #请求头-Authorization
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token or token == 'null':
            return JsonResponse({'code':403,'error':'please login'})
        #校验token
        try:
            res = jwt.decode(token,settings.JWT_TOKEN_KEY)
        except Exception as e:
            print(e,'检验登录的时候校验token出错')
            return JsonResponse({'code':403,'error':'please login'})
        username = res['username']
        user = User.objects.get(username=username)
        request.myuser = user
        return func(request,*args,**kwargs)
    return wrap




