from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import UserInfo

# Create your views here.

def Index(request):
    username = ''
    try:
        username = request.session['username']
        user = 0
    except:
        user = 1
    context = {
        'user': user,
        'username': username,
    }
    return render(request, 'users/index.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([id, username, password]):
            return HttpResponse('参数不全')
        # 业务处理： 登录校验
        try:
            User = UserInfo.objects.get(username=username)
            if User.is_active:
                # 用户已激活
                request.session['username'] = username
                # index = 0
                # context = {
                #     'user': index,
                #     'username': username
                # }
                # response = render(request, 'users/index.html', context)
                response = redirect(reverse('users:index'))
                remember = request.POST.get('remember')
                if remember == 'on':
                    # 记住用户名
                    response.set_cookie('username', username, max_age=24*3600)
                else:
                    # 下次不需要记住
                    response.delete_cookie('username')
                return response
            else:
                index = 1
                context = {
                    'user': index,
                    # 'message': '用户未激活'
                }
                return render(request, 'users/index.html', context)
        except UserInfo.DoesNotExist:
            index = 1
            context = {
                'user': index,
                # 'message': '没有该用户'
            }
            return render(request, 'users/index.html', context)
        # else:
        #     # 校验用户是否重复
        #     try:
        #         User = UserInfo.objects.get(username=username)
        #         index = 0
        #     except UserInfo.DoesNotExist:
        #         # 用户名不存在
        #         username = ''
        #         index = 1
        #     context = {
        #         'user': index,
        #         'username': username
        #     }
        #     # return redirect(reverse('users:index'), context)
        #     return render(request, 'users/index.html', context)
    else:
        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
        else:
            username = ''
        return render(request, 'users/login.html', {'username': username})

def Logout(request):
    del request.session['username']
    return redirect(reverse('users:index'))


def Register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not all([id, username, password, email]):
            return HttpResponse('参数不全')

        # 检查用户名是否重复
        User = UserInfo.objects.filter(username=username)
        if not len(User):
            user = UserInfo()
            user.username = username
            user.password = password
            user.email = email
            user.is_active = True
            user.save()
            request.session['username'] = username
            return redirect(reverse('users:index'))
        else:
            return HttpResponse('用户名重复')