from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class register_forms(forms.ModelForm):
	username = forms.CharField(
		label='用户名', required=True, error_messages={
		'required':'请填写你的用户名', 'min_length':'至少输入3个字符', 'max_length':'最多只能输入15个字符'
		},
		min_length=3, max_length=15, widget=forms.TextInput(attrs={'placeholder':'3~15位字母/数字/汉字'})
		)
	password = forms.CharField(
		label='密码', required=True, error_messages={
		'required':'请填写你的密码', 'min_length':'至少输入6个字符', 'max_length':'最多只能输入20个字符'
		},
		min_length=6, max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'长度在6~20个字符以内'})
		)
	confirm_password = forms.CharField(
		label='确认密码', required=True, error_messages={
		'required':'请填写你的确认密码', 'min_length':'至少输入6个字符', 'max_length':'最多只能输入20个字符'
		},
		min_length=6, max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'长度在6~20个字符以内'})
		)

	class Meta:
		model = get_user_model()
		fields = ('username', 'password')

	def clean_username(self):
		UserModel = get_user_model()
		username = self.cleaned_data['username']

		try:
			UserModel.objects.get(username=username)
		except UserModel.DoesNotExist:
			return username
		raise forms.ValidationError('已经有人注册该用户名')

	def clean_confirm_password(self):
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']

		if password != confirm_password:
			raise forms.ValidationError('两次输入的密码不一致')
		return confirm_password

class user_change_forms(UserChangeForm):
	name = forms.CharField(
		required=False,
		min_length=3, max_length=10, widget=forms.TextInput(attrs={'placeholder':'3~10位字母/数字/汉字'})
		)
	gender = forms.CharField(required=False)
	birthday = forms.DateField(required=False)

	class Meta:
		model = User
		fields = ('username', 'password', 'name', 'gender', 'birthday')

	def clean_gender(self):
		gender = self.cleaned_data['gender']

		if gender == '1':
			return '男'
		elif gender == '2':
			return '女'
		elif gender == '3':
			return '保密'

