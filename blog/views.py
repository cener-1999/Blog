from django.shortcuts import render
from .models import *
import markdown
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.http import JsonResponse

# Create your views here.

def post(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        # TODO: msg box
        return JsonResponse({'success': False, 'msg': "can not find it"})

    # test
    print()
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ]
    )
    post.body = md.convert(post.body)
    f = open('text.md',encoding='utf-8',mode='w')
    f.write(post.body)
    return render(request,"blog/post.html",{'post':post})


def classify(request,type):
    post_list = Post.objects.filter(category__name=type)
    if len(post_list)==0:
        return JsonResponse({'success': False, 'msg': "{}分类下没有文章".format(type)})
    return render(request,'blog/index.html',{'post_list':post_list})

def tags(request,tag):
    post_list = Post.objects.filter(tags__name=tag)
    if len(post_list) == 0:
        return JsonResponse({'success': False, 'msg': "没有文章有{}标签".format(tag)})
    return render(request,'blog/index.html',{'post_list':post_list})

def author(request,name):
    post_list = Post.objects.filter(author__username=name)
    if len(post_list) == 0:
        return JsonResponse({'success': False, 'msg': "用户{}没有文章".format(name)})
    return render(request,'blog/index.html',{'post_list':post_list})
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',{'post_list':post_list})

