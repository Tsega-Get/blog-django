from xml.dom.minidom import Identified
from django.shortcuts import render
from django.urls import reverse
from datetime import date
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.template.loader import render_to_string


from .models import Post

all_posts = [
   
]
def get_date(post):
    return post['date']
    
# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] 
    return render(request, "blog/index.html", {
       "posts":latest_posts 
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request, slug):
    try:
        identified_posts = next(post for post in all_posts if post['slug']==slug)
        return render(request, "blog/post-detail.html", {
            "post" : identified_posts
        })
    except:
       # raise Http404()
       response_data =  render_to_string("404.html") 
       return HttpResponseNotFound(response_data) 
            