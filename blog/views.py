from django.shortcuts import render
from .models import *
import markdown
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.http import JsonResponse

# Create your views here.

def post(request,pk):
    try:
        data = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        # TODO: msg box
        return JsonResponse({'success': False, 'msg': "can not find it"})

    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ]
    )
    data.body = md.convert(data.body)
    f = open('text.md',encoding='utf-8',mode='w')
    f.write(data.body)
    return render(request,"blog/post.html",{'data':data})


def index(request):
    return render(request,'blog/index.html')