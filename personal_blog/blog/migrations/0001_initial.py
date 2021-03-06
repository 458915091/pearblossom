# Generated by Django 2.1.3 on 2019-01-28 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('clicks', models.IntegerField(default=0, verbose_name='阅读数')),
                ('num', models.IntegerField(verbose_name='博客编码')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '博客',
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15, verbose_name='类型名称')),
            ],
            options={
                'verbose_name_plural': '博客类型',
                'db_table': 'blog_type',
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carouse_name', models.CharField(max_length=15, verbose_name='轮播名称')),
                ('title1', models.CharField(max_length=20, verbose_name='标题1')),
                ('image1', models.ImageField(upload_to='blog/carousel/%Y.%m.%d', verbose_name='图1')),
                ('url1', models.CharField(max_length=50, verbose_name='圖1 url')),
                ('title2', models.CharField(max_length=20, verbose_name='标题2')),
                ('image2', models.ImageField(upload_to='blog/carousel/%Y.%m.%d', verbose_name='图2')),
                ('url2', models.CharField(max_length=50, verbose_name='圖2 url')),
                ('title3', models.CharField(max_length=20, verbose_name='标题3')),
                ('image3', models.ImageField(upload_to='blog/carousel/%Y.%m.%d', verbose_name='图3')),
                ('url3', models.CharField(max_length=50, verbose_name='圖3 url')),
                ('title4', models.CharField(max_length=20, verbose_name='标题4')),
                ('image4', models.ImageField(upload_to='blog/carousel/%Y.%m.%d', verbose_name='图4')),
                ('url4', models.CharField(max_length=50, verbose_name='圖4 url')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'db_table': 'carousel',
            },
        ),
        migrations.CreateModel(
            name='Publicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicity_name', models.CharField(max_length=15, verbose_name='推广名称')),
                ('title1', models.CharField(max_length=20, verbose_name='标题1')),
                ('image1', models.ImageField(upload_to='blog/publicity/%Y.%m.%d', verbose_name='图1')),
                ('url1', models.CharField(max_length=50, verbose_name='圖1 url')),
                ('title2', models.CharField(max_length=20, verbose_name='标题2')),
                ('image2', models.ImageField(upload_to='blog/publicity/%Y.%m.%d', verbose_name='图2')),
                ('url2', models.CharField(max_length=50, verbose_name='圖2 url')),
                ('title3', models.CharField(max_length=20, verbose_name='标题3')),
                ('image3', models.ImageField(upload_to='blog/publicity/%Y.%m.%d', verbose_name='图3')),
                ('url3', models.CharField(max_length=50, verbose_name='圖3 url')),
                ('title4', models.CharField(max_length=20, verbose_name='标题4')),
                ('image4', models.ImageField(upload_to='blog/publicity/%Y.%m.%d', verbose_name='图4')),
                ('url4', models.CharField(max_length=50, verbose_name='圖4 url')),
                ('title5', models.CharField(max_length=20, verbose_name='标题5')),
                ('image5', models.ImageField(upload_to='blog/publicity/%Y.%m.%d', verbose_name='图5')),
                ('url5', models.CharField(max_length=50, verbose_name='圖5 url')),
                ('title6', models.CharField(max_length=20, verbose_name='标题6')),
                ('image6', models.ImageField(upload_to='blog/publicity/%Y.%m.%d', verbose_name='图6')),
                ('url6', models.CharField(max_length=50, verbose_name='圖6 url')),
                ('title7', models.CharField(max_length=20, verbose_name='标题7')),
                ('image7', models.ImageField(upload_to='blog/publicity/%Y.%m.%d', verbose_name='图7')),
                ('url7', models.CharField(max_length=50, verbose_name='圖7 url')),
                ('title8', models.CharField(max_length=20, verbose_name='标题8')),
                ('image8', models.ImageField(upload_to='blog/publicity/%Y.%m.%d', verbose_name='图8')),
                ('url8', models.CharField(max_length=50, verbose_name='圖8 url')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '宣传栏',
                'db_table': 'publicity',
            },
        ),
        migrations.CreateModel(
            name='user_imformations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称')),
                ('gender', models.CharField(max_length=4, null=True, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('head', models.ImageField(null=True, upload_to='blog/head', verbose_name='头像')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '用户信息名单',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.BlogType'),
        ),
    ]
