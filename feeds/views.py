from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Posts
from django.urls import reverse
from datetime import datetime

def index(request):
    post = Posts.objects.all().values()
    template = loader.get_template('posts.html')
    context = {
     'allposts': post,
    }
    return HttpResponse(template.render(context, request))
    
def add_post(request):
    name = request.POST['name']
    post = request.POST['post']
    time = datetime.now().strftime('%a %d, %b %Y - %I:%M%p')

    post = Posts(name=name, post=post, time=time)
    post.save()
    return HttpResponseRedirect(reverse('index'))