from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def login(request):
    if request.session.get('is_login', None):  # 如果没有名为is_login的session
        return redirect('/index/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写内容"
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']  # None is default value
            password = login_form.cleaned_data['password']
        try:
            user = models.User.objects.get(name=username)
            if user.password == password:
                request.session['is_login'] =True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name           
                return redirect('/index/')
            else:
                message = "密码不正确"
        except:
            message = "用户名不存在"
        return render(request, 'login/login.html', locals())
    
    else:  # 非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户填入数据
        login_form = forms.UserForm()
        return render(request, 'login/login.html', locals())

# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)  # None is default value
#         password = request.POST.get('password', None)
#         message = "所有字段都必须填写"
#          
#         if username and password:
#             username = username.strip()
#         try:
#             user = models.User.objects.get(name=username)
#             if user.password == password:
#                 return render(request, 'login/index.html')
#             else:
#                 message = "密码不正确"
#         except:
#             message = "用户名不存在"
#         return render(request, 'login/login.html', {"message": message})
#     
#     else:
#         return render(request, 'login/login.html')

def register(request):
    pass
    return render(request, 'login/register.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect('/index/')