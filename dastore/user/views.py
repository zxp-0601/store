import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import User
from tools.mytools import data_md5,make_token,make_code,logging_check
from django.core.cache import cache
from .tasks import send_sms


# def get_info(request,username):
#     return JsonResponse({'code':200,'username':username,'data':{'info':'你好'}})

class UsersView(View):
    #get请求，得到用户相关信息
    def get(self,request,username):
        print(request.body)
        return JsonResponse({'code': 200, 'username': username, 'data': {'info': '你好'}})


    #post请求，用户通过邮箱注册使用
    def post(self,request:HttpRequest):
        #通过响应体拿到json串，并转化为Python类型
        json_str = request.body
        json_obj = json.loads(json_str)
        #拿到前端框里输入的内容
        username = json_obj['username']
        email = json_obj['email']
        sms_num = json_obj['sms_num']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']

        #进行一系列的判断
        #如果有一个框里没填，就返回错误
        if not username or not email or not sms_num or not phone or not password_1 or not password_2:
            return JsonResponse({'code':10000,'error':'请输入完整的信息'})
        #如果用户名超过12个长度就报错
        if len(username) >12:
            return JsonResponse({'code':10001,'error':'用户名不能超过12个字符'})
        #检查用户名是否可用
        old_user = User.objects.filter(username=username)
        if old_user:
            return JsonResponse({'code':10002,'error':'用户名已存在'})
        #检查验证码是否正确
        cache_key = 'sms_{}'.format(email)
        old_code = cache.get(cache_key)
        if old_code != sms_num:
            return JsonResponse({'code':10007,'error':'验证码错误'})
        #对密码进行验证
        if password_2 !=password_1:
            return JsonResponse({'code':10003,'error':'两次密码不一致'})
        #对密码进行md5加密并存入数据库
        password_h = data_md5(password_1)
        print('--------------------')
        print(password_h,json_obj)
        try:
            user = User.objects.create(username=username,password=password_h,email=email,phone=phone)
        except Exception as e:
            print(e,'注册时插入数据库的报错')
            return JsonResponse({'code':10004,'error':'未创建成功，请重新尝试'})
        # 签发token
        token = make_token(username)

        return JsonResponse({'code':200,'username':username,'data':{'token':token.decode()}})


def sms_view(request):
    """异步发送邮件"""
    #从响应体里拿到email
    json_str = request.body
    json_obj = json.loads(json_str)
    email = json_obj['email']

    #验证是否有输入邮箱
    if not email:
        return JsonResponse({'code':10008,'error':'请输入正确的邮箱'})
    #检查当前邮箱是否已经注册
    old_email = User.objects.filter(email=email)
    if old_email:
        return JsonResponse({'code':10005,'error':'当前邮箱已经注册'})
    #检查当前邮箱有没有已经存在的验证码
    cache_key = 'sms_{}'.format(email)
    old_code = cache.get(cache_key)
    if old_code:
        return JsonResponse({'code':10006,'error':'验证码已经发送'})
    #生成验证码
    code = make_code()
    print(code,'111111111111111111111')
    #存储验证码65s
    cache.set(cache_key,code,65)
    #采用异步发送
    send_sms.delay(email,code)

    return JsonResponse({'code':200})

def login_view(request:HttpRequest):
    json_str = request.body
    json_obj = json.loads(json_str)

    username = json_obj['username']
    password = json_obj['password']

    if not username or not password:
        return JsonResponse({'code':10100,'error':'用户名或者密码错误'})
    # 判断用户名是否已经注册
    try:
        user = User.objects.get(username=username)
    except Exception as e:
        print(e,'登录时判断用户名是否注册的错误')
        return JsonResponse({'code':10101,'error':'用户名未注册'})
    #判断密码是否正确
    password_h = data_md5(password)
    if password_h != user.password:
        return JsonResponse({'code':10102,'error':'用户名或者密码错误！'})
    #签发token
    token = make_token(username)
    return JsonResponse({'code':200,'username':username,'data':{'token':token.decode()}})