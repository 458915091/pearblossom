from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.
class BlogType(models.Model):
	type_name = models.CharField('类型名称', max_length=15)

	class Meta:
		verbose_name_plural = '博客类型'
		db_table = 'blog_type'

	def __str__(self):
		return self.type_name

class Blog(models.Model):
	title = models.CharField('标题', max_length=20)
	author = models.OneToOneField(User, on_delete=models.CASCADE)
	blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
	content = models.TextField('内容', )
	create_time = models.DateTimeField('创建时间', auto_now_add=True)
	update_time = models.DateTimeField('更新时间', auto_now=True)
	clicks = models.IntegerField('阅读数', default=0)
	num = models.IntegerField('博客编码', default=random.randint(10000,99999))

	class Meta:
		verbose_name_plural = '博客'
		db_table = 'blog'

	def __str__(self):
		return self.title

class Carousel(models.Model):
	carouse_name = models.CharField('轮播名称', max_length=15)

	title1 = models.CharField('标题1', max_length=20) 
	image1 = models.ImageField('图1', upload_to='blog/carousel/%Y.%m.%d')
	url1 = models.CharField('圖1 url', max_length=50,blank=True, null=True)

	title2 = models.CharField('标题2', max_length=20)
	image2 = models.ImageField('图2', upload_to='blog/carousel/%Y.%m.%d')
	url2 = models.CharField('圖2 url', max_length=50,blank=True, null=True)

	title3 = models.CharField('标题3', max_length=20) 
	image3 = models.ImageField('图3', upload_to='blog/carousel/%Y.%m.%d')
	url3 = models.CharField('圖3 url', max_length=50,blank=True, null=True)

	title4 = models.CharField('标题4', max_length=20)
	image4 = models.ImageField('图4', upload_to='blog/carousel/%Y.%m.%d')
	url4 = models.CharField('圖4 url', max_length=50,blank=True, null=True)
	
	create_time = models.DateTimeField('创建时间', auto_now_add=True)

	class Meta:
		verbose_name_plural = '轮播图'
		db_table = 'carousel'

	def __str__(self):
		return self.carouse_name

class Publicity(models.Model):
	publicity_name = models.CharField('推广名称', max_length=15)
	title1 = models.CharField('标题1', max_length=20)
	image1 = models.ImageField('图1', upload_to='blog/publicity/%Y.%m.%d')
	url1 = models.CharField('圖1 url', max_length=50,blank=True, null=True)

	title2 = models.CharField('标题2', max_length=20) 
	image2 = models.ImageField('图2', upload_to='blog/publicity/%Y.%m.%d')
	url2 = models.CharField('圖2 url', max_length=50,blank=True, null=True)

	title3 = models.CharField('标题3', max_length=20) 
	image3 = models.ImageField('图3', upload_to='blog/publicity/%Y.%m.%d')
	url3 = models.CharField('圖3 url', max_length=50,blank=True, null=True)

	title4 = models.CharField('标题4', max_length=20)
	image4 = models.ImageField('图4', upload_to='blog/publicity/%Y.%m.%d')
	url4 = models.CharField('圖4 url', max_length=50,blank=True, null=True)

	title5 = models.CharField('标题5', max_length=20) 
	image5 = models.ImageField('图5', upload_to='blog/publicity/%Y.%m.%d')
	url5 = models.CharField('圖5 url', max_length=50,blank=True, null=True)

	title6 = models.CharField('标题6', max_length=20) 
	image6 = models.ImageField('图6', upload_to='blog/publicity/%Y.%m.%d')
	url6 = models.CharField('圖6 url', max_length=50,blank=True, null=True)

	title7 = models.CharField('标题7', max_length=20) 
	image7 = models.ImageField('图7', upload_to='blog/publicity/%Y.%m.%d')
	url7 = models.CharField('圖7 url', max_length=50,blank=True, null=True)

	title8 = models.CharField('标题8', max_length=20)
	image8 = models.ImageField('图8', upload_to='blog/publicity/%Y.%m.%d')
	url8 = models.CharField('圖8 url', max_length=50,blank=True, null=True)
 
	create_time = models.DateTimeField('创建时间', auto_now_add=True)

	class Meta:
		verbose_name_plural = '宣传栏'
		db_table = 'publicity'

	def __str__(self):
		return self.publicity_name

class user_imformations(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField('昵称', blank=True, null=True, max_length=20) 
	gender = models.CharField('性别', max_length=4, null=True)
	birthday = models.DateField('生日', blank=True, null=True)
	head = models.ImageField('头像', upload_to='blog/head', null=True)

	class Meta:
		verbose_name_plural = "用户信息名单"

	def __str__ (self):
		return ""