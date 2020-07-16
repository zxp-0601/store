#######################################
#               file_name:flask_client.py
#               author:zxp
#               mail:577603561@qq.com
######################################


from flask import Flask,send_file
import sys

app = Flask(__name__)

@app.route('/index')
def index():
    #首页
    return send_file('templates/index.html')

@app.route('/login')
def login():
    #登录
    return send_file('templates/login.html')

@app.route('/register')
def register():
    #注册
    return send_file('templates/register.html')

@app.route('/<username>/info')
def info(username):
    #个人信息
    return send_file('templates/about.html')

@app.route('/<username>/change_info')
def change_info(username):
    #修改个人信息
    return send_file('templates/change_info.html')

@app.route('/<username>/change_password')
def change_password(username):
    #修改密码
    return send_file('templates/change_password.html')










if __name__ == '__main__':
    app.run(debug=True)