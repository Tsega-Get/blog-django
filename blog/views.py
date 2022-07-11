from django.shortcuts import render, get_object_or_404 
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.template.loader import render_to_string


from .models import Post
 

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] 
    return render(request, "blog/index.html", {
       "posts":latest_posts 
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request, slug):
    
    identified_post = get_object_or_404(Post, slug = slug)
    return render(request, "blog/post-detail.html", {
            "post" : identified_post,
            "post_tags":identified_post.tags.all()
    })   
    
    # try:
    #     # identified_post = Post.objects.get(slug = slug)
    #     # identified_posts = next(post for post in all_posts if post['slug']==slug)
    #     identified_post = get_list_or_404(Post, slug = slug)
    #     return render(request, "blog/post-detail.html", {
    #         "post" : identified_post
    #     })
    # except:
    #    # raise Http404()
    #    response_data =  render_to_string("404.html") 
    #    return HttpResponseNotFound(response_data) 
            