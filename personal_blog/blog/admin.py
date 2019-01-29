from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import *

# Register your models here.
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['id','type_name']

admin.site.register(BlogType, BlogTypeAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'blog_type', 'create_time', 'update_time']

admin.site.register(Blog, BlogAdmin)

class CarouselAdmin(admin.ModelAdmin):
    list_display = ['carouse_name', 'title1', 'title2', 'title3', 'title4', 'create_time']

admin.site.register(Carousel, CarouselAdmin)

class PublicityAdmin(admin.ModelAdmin):
    list_display = ['publicity_name', 'title1', 'title2', 'title3', 'title4',  'create_time']

admin.site.register(Publicity, PublicityAdmin)

class UserFromAdmin(admin.TabularInline):
	model = user_imformations
	can_delect = False
	verbose_name_plural = '用户信息'

class UserAdmin(BaseUserAdmin):
	inlines = [UserFromAdmin,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)