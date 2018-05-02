# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def homepage(request):
    template=get_template('index.html')
    posts = Post.objects.all()
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)
    #post_lists=list()
    #for count,post in enumerate(posts):
    #    post_lists.append("No.{}:".format(str(count))+str(post.body.encode('utf-8'))+"<hr>")
    #    post_lists.append("<small>"+str(post.body.encode('utf-8'))+"</small><br><br>")
    #return HttpResponse(post_lists)


def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post != None:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
