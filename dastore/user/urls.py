from django.urls import path

from user import views

urlpatterns = [
    #http://127.0.0.1:8000/v1/users/sms
    path('sms',views.sms_view),
    # 'http://127.0.0.1:8000/v1/users/login'
    path('login',views.login_view),
    #"http://127.0.0.1:8000/v1/users/"+ username
    path('<str:username>',views.UsersView.as_view())
]


# <script  charset="utf-8">
#       //var url = document.location.toString();
#       //var arrUrl = url.split("//");
#
#       //var blog_username = arrUrl[1].split('/')[1];
#       var html_body = '';
#       token = window.localStorage.getItem('dstore_token');
#       //登陆的用户名
#       username = window.localStorage.getItem('dstore_user');
#       console.log(username)
#
#       $.ajax({
#          // 请求方式
#          type:"get",
#          // url
#          url:"http://127.0.0.1:8000/v1/users/"+ username,
#          beforeSend: function(request) {
#              request.setRequestHeader("Authorization", token);
#          },
#          success:function (result) {
#              if (200 == result.code){
#                  $(document).attr('title', '关于'+ username+'的个人信息');
#                  header_html = makeHeader(username)
#                  html_body += header_html
#
#                  html_body += '<h1 ><span>个人信息</span>';
#                  html_body += '<p>关于我</p>';
#                  html_body += '</h1>';
#                  html_body += '<div >';
#                  //个人描述
#                  html_body += '<ul>';
#                  if(result.data.info){
#                     html_body += result.data.info;
#                  }else{
#                     html_body += '空空如也'
#                  }
#                  html_body += '</ul>';
#                  html_body += '</div>';
#
#                  //avatar
#                  if (result.data.avatar) {
#                      var avatar_url = 'http://127.0.0.1:8000/media/'+ result.data.avatar;
#                      html_body += '<p class="avatar"> <img src=' + avatar_url + ' alt=""> </p>';
#                  }else{
#                      html_body += '<p class="avatar"> <img src="/static/images/avatar.jpg" alt=""> </p>';
#                  }
#                  //username
#                  html_body += '<p>';
#                  html_body += result.username;
#                  html_body += '</p>';
#
#
#
#                  //footer
#
#                  html_body += '<p>Design by <a href=# target="_blank">';
#                  html_body += "zxp";
#                  html_body += '</a>';
#                  html_body += '</footer>';
#                  $('body').html(html_body);
#                  //初始化登出事件
#                  loginOut()
#
#                  //下拉菜单
#                  $('.nav>li').hover(function () {
#                      $(this).children('ul').stop(true, true).show(400);
#                  }, function () {
#                      $(this).children('ul').stop(true, true).hide(400);
#                  });
#              }else{
#                  alert(result.error)
#              }
#          }
#     });
#     </script>