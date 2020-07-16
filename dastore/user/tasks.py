from dastore.celery import app
# from tools.mytools import send_email
from django.core import mail


def send_email(email,code):
    """发送邮件"""
    mail.send_mail(
        '注册验证码,3分钟有效',
        code,
        '577603561@qq.com',
        recipient_list=[email],
    )
    print('邮件已经发送')

@app.task
def send_sms(email,code):
    res = send_email(email,code)
    return res