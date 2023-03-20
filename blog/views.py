from django.shortcuts import render
from .models import *
import markdown
import re
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
import openai


def post(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        # TODO: msg box
        return JsonResponse({'success': False, 'msg': "can not find it"})

    comment_list = Comment.objects.filter(post=post)
    comment_num = len(comment_list)

    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            "markdown.extensions.toc",
            "markdown.extensions.sane_lists",
            TocExtension(slugify=slugify),
        ]
    )
    # TODO: make \n bette
    # print(repr(post.body))
    # post.body = post.body.replace('\r\n\r\n', '\r\n\r\n<br>\r\n\r\n')
    # print(repr(post.body))

    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request,"blog/post.html",{'post':post,'comment_list':comment_list,'comment_num':comment_num})


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

def archive(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,created_time__month=month,).order_by('-created_time')
    return render(request,'blog/index.html',{'post_list':post_list})

def make_comment(request,post_pk):
    username = request.POST.get('name')
    content = request.POST.get('comment')
    post = Post.objects.get(id=post_pk)
    c = Comment(
        username = username,
        content = content,
        post = post
    )
    c.save()
    return HttpResponseRedirect('/post/{}'.format(post_pk))



def get_gpt(request):
    openai.api_key = "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"
    if request.method == 'POST':
        user_input = request.POST['user_input']
        response = openai.Completion.create(
          engine="davinci",
          prompt=user_input,
          max_tokens=1024,
          n=1,
          stop=None,
          temperature=0.5,
        )
        output = response.choices[0].text.strip()
        return render(request, 'gpt.html', {'user_input': user_input, 'output': output})
    else:
        return render(request, 'gpt.html')
