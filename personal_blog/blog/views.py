from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import * 
from .form import *
import random

# Create your views here.

# 主页
def home(request):
	content={}
	content['carousel'] = Carousel.objects.all()
	content['publicity'] = Publicity.objects.all()
	content['new'] = Blog.objects.order_by("-update_time")[:8]
	content['ranking'] = Blog.objects.order_by("-clicks")[:8]
	content['random'] = Blog.objects.order_by("?")[:8]
	return render(request, 'blog/home.html', content)

# 随笔详情页
def detail(request, author, num):
	content={}
	try:
		content['detail'] = Blog.objects.get(num=num)
		return render(request, 'blog/detail.html', content)
	except:
		return render(request, 'blog/404.html')

# 随笔添加页
@login_required(login_url='blog:login')
def add(request):
	content={}
	content['type'] = BlogType.objects.all()
	# print(BlogType.objects.all())

	if request.method == 'POST':
		print(request.POST)
		title = request.POST['title']
		blog_content = request.POST['content']

		content['title'] = title
		content['content'] = blog_content

		if request.POST['title'] == '':
			content['error'] = '错误信息：请输入博客标题！'

		elif request.POST['blog_type'] == '0':
			content['error'] = '错误信息：请选择博客类型！'
		

		elif request.POST['content'] == '':
			content['error'] = '错误信息：请输入博客内容！'

		else:

			blog_type = BlogType.objects.get(id=request.POST['blog_type'])
			num = random.randint(10000,99999)
			add_row = Blog(title=title, content=blog_content, author=request.user, blog_type=blog_type, num=num)
			add_row.save()

			seach = Blog.objects.get(num=num)
			author = seach.author
			return redirect('blog:detail', author, num)

		return render(request, 'blog/add.html', content)

	elif request.method == 'GET':
		return render(request, 'blog/add.html', content)

# 用户注册页
def register(request):
	if request.method =='POST':
		forms = register_forms(request.POST)
		if forms.is_valid():
			user = get_user_model()
			username = forms.cleaned_data['username']
			confirm_password = forms.cleaned_data['confirm_password']

			add_user = user.objects.create_user(username=username, password=confirm_password)
			add_user.save()
			auth_user = authenticate(username=username, password=confirm_password)

			imformations = user_imformations(user=auth_user)
			imformations.save()
			
			login(request, auth_user)
			return redirect('blog:home')

	elif request.method == 'GET':
		forms = register_forms()

	content = {}
	content['form'] = forms
	return render(request, 'blog/register.html', content)

# 用户登陆页
def user_login(request):
	if request.method == 'POST':
		login_form = AuthenticationForm(data=request.POST)
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

		if login_form.is_valid():
			user = authenticate(request, username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
			login(request, user)
			return redirect('blog:home')
		else:
			content = {}
			content['errors'] = '用户名或密码错误'
			content['form'] = login_form
			return render(request, 'blog/login.html', content)

	elif request.method == 'GET':
		login_form = AuthenticationForm()

	content = {}
	content['form'] = login_form
	return render(request, 'blog/login.html', content)

# 用户登出
@login_required(login_url='blog:login')
def user_logout(request):
	logout(request)
	return redirect('blog:home')

# 个人中心
@login_required(login_url='blog:login')
def center(request):
	if request.method == 'POST':

		if request.POST.get('name'):
			change_forms = user_change_forms(request.POST, instance=request.user)

			if change_forms.is_valid():
				name = change_forms.cleaned_data['name']
				gender = change_forms.cleaned_data['gender']
				birthday = change_forms.cleaned_data['birthday']
				request.user.user_imformations.name = name
				request.user.user_imformations.gender = gender
				request.user.user_imformations.birthday = birthday
		else:
			request.user.user_imformations.head = request.FILES.get('avatar')

		request.user.user_imformations.save()
		return redirect('blog:center')

	elif request.method == 'GET':
		user_content = request.user

	content = {}
	# content['user'] = user_content
	return render(request, 'blog/center.html', content)
